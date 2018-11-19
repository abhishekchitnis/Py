package webdriver;

import com.sun.org.apache.xalan.internal.xsltc.runtime.Hashtable;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.PrintStream;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Iterator;
import java.util.concurrent.TimeUnit;
import javax.swing.JOptionPane;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import org.ini4j.Ini;
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.UnexpectedAlertBehaviour;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebDriver.Options;
import org.openqa.selenium.WebDriver.Timeouts;
import org.openqa.selenium.WebDriver.Window;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.firefox.FirefoxProfile;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.remote.DesiredCapabilities;

public class RQMUploadUtility
{
  private WebDriver driver;
  private Actions action;
  private String baseUrl;
  private String sTestCaseFile;
  private StringBuffer verificationErrors = new StringBuffer();
  private static String userid; private static String passwd; private static String EnvPath; private static String sLogFileName; private static String TestCaseName = null;
  
  public RQMUploadUtility() {}
  
  public static void main(String[] args) { EnvPath = args[0];
    
    System.out.println("TestCase Upload Starts");
    RQMUploadUtility RQMupload = new RQMUploadUtility();
    
    try
    {
      sLogFileName = EnvPath + "\\LogFiles\\Log_" + new SimpleDateFormat("dd-MM-YYYY_hh_mm_ss a").format(new Date()) + ".txt";
      RQMupload.setUp();
      RQMupload.AutoUpload();
      RQMupload.tearDown();
    }
    catch (Exception e)
    {
      System.out.println("Error : " + e.getCause() + " Message : " + e.getMessage());
    }
  }
  

  public void setUp()
    throws Exception
  {
    Ini oIni = new Ini(new File(EnvPath + "\\RQM_Utility_Config.txt"));
    String sBrowserName = oIni.get("Environment", "Browser");
    sTestCaseFile = oIni.get("Environment", "TestCaseFileName");
    baseUrl = oIni.get("Environment", "RQMUrl");
    userid = oIni.get("Environment", "RQMUserName");
    passwd = oIni.get("Environment", "RQMUserPassword");
    


    if (sBrowserName.equalsIgnoreCase("FIREFOX"))
    {

      Hashtable prefs = new Hashtable();
      prefs.put("download.prompt_for_download", Boolean.valueOf(true));
      DesiredCapabilities cap = new DesiredCapabilities();
      cap.setCapability("unexpectedAlertBehaviour", UnexpectedAlertBehaviour.IGNORE);
      cap.setCapability("ignoreProtectedModeSettings", true);
      cap.setCapability("prefs", prefs);
      FirefoxProfile fp = new FirefoxProfile();
      fp.setPreference("plugin.default.state", 2);
      fp.setPreference("plugin.state.java", 2);
      fp.setPreference("security.enable_java", true);
      cap.setCapability("firefox_profile", fp);
      driver = new org.openqa.selenium.firefox.FirefoxDriver(cap);
      driver.manage().timeouts().implicitlyWait(50L, TimeUnit.SECONDS);
      driver.manage().window().maximize();
    }
    else if (sBrowserName.equalsIgnoreCase("CHROME"))
    {
      File chromeFile = new File(EnvPath + "\\Library\\chromedriver.exe");
      
      System.setProperty("webdriver.chrome.driver", chromeFile.getAbsolutePath());
      Hashtable prefs = new Hashtable();
      prefs.put("download.prompt_for_download", Boolean.valueOf(true));
      
      ChromeOptions options = new ChromeOptions();
      

      options.addArguments(new String[] { "--always-authorize-plugins=true" });
      options.setExperimentalOption("prefs", prefs);
      driver = new org.openqa.selenium.chrome.ChromeDriver(options);
      driver.manage().timeouts().implicitlyWait(50L, TimeUnit.SECONDS);
      driver.manage().window().maximize();
    }
    else if (sBrowserName.equalsIgnoreCase("IE"))
    {
      File chromeFile = new File(EnvPath + "\\Library\\IEDriverServer_64Bit.exe");
      System.setProperty("webdriver.ie.driver", chromeFile.getAbsolutePath());
      Hashtable prefs = new Hashtable();
      prefs.put("download.prompt_for_download", Boolean.valueOf(true));
      DesiredCapabilities cap = new DesiredCapabilities();
      cap.setCapability("unexpectedAlertBehaviour", UnexpectedAlertBehaviour.IGNORE);
      cap.setCapability("ignoreProtectedModeSettings", true);
      cap.setCapability("prefs", prefs);
      driver = new org.openqa.selenium.ie.InternetExplorerDriver(cap);
    }
    else
    {
      throw new Exception("unable to launch the URL for Browser" + sBrowserName);
    }
  }
  
  public void AutoUpload() throws Exception
  {
    action = new Actions(driver);
    login(userid, passwd);
    String name = null;String desc = null;String pre = null;String post = null;String step = null;String exp = null;String functionalGroup = null;String SubFunctionGroup = null;String Failureimpact = null;String FailureLikly = null;
    Thread.sleep(2000L);
    String sFileName = EnvPath + "\\TestCases\\" + sTestCaseFile;
    FileInputStream file = new FileInputStream(sFileName);
    
    XSSFWorkbook workbook = new XSSFWorkbook(file);
    XSSFSheet sheet = workbook.getSheet("TestCases");
    Iterator<Row> rowIterator = sheet.iterator();
    boolean new_record = false;
    
    while (rowIterator.hasNext())
    {
      Row row = (Row)rowIterator.next();
      if (row.getRowNum() != 0)
      {
        new_record = false;
        if (!row.getCell(0).getStringCellValue().equalsIgnoreCase(""))
        {
          if (row.getRowNum() != 1)
          {
            driver.findElement(By.xpath("//div[@id='com_ibm_asq_common_web_ui_internal_view_layout_ViewHeaderLayout_1']/div[2]/div/div/button[2]")).click();
            Thread.sleep(4000L);
          }
          
          writeLogs("********************** New TestCase **********************************");
          writeLogs("TestCase : = " + row.getCell(0).getStringCellValue());
          writeLogs("TimeStamp : = " + new SimpleDateFormat("dd-MM-YYYY_hh_mm_ss a").format(new Date()));
          writeLogs("*********************************************************************");
          new_record = true;
          if ((TestCaseName != null) && (!TestCaseName.equalsIgnoreCase("")))
          {
            writeLogs("********************************************************");
            writeLogs(TestCaseName + " :::: Test Cases is uploaded");
            writeLogs("*********************************************************");
          }
          TestCaseName = row.getCell(0).getStringCellValue();
          name = row.getCell(0).getStringCellValue();
          desc = row.getCell(1).getStringCellValue();
          pre = row.getCell(2).getStringCellValue();
          post = row.getCell(3).getStringCellValue();
          step = row.getCell(4).getStringCellValue();
          exp = row.getCell(5).getStringCellValue();
          functionalGroup = row.getCell(6).getStringCellValue();
          SubFunctionGroup = row.getCell(7).getStringCellValue();
          Failureimpact = row.getCell(8).getStringCellValue();
          FailureLikly = row.getCell(9).getStringCellValue();
          
          driver.get(baseUrl);
          summary(name, desc, functionalGroup, SubFunctionGroup, Failureimpact, FailureLikly);
          description(desc);
          pre_condition(pre);
          post_condition(post);
          test_script(name, desc);
          test_step(step, exp);
        }
        else
        {
          step = row.getCell(4).getStringCellValue();
          exp = row.getCell(5).getStringCellValue();
          action.keyDown(Keys.CONTROL).perform();
          action.sendKeys(new CharSequence[] { Keys.ENTER }).perform();
          action.keyUp(Keys.CONTROL).perform();
          Thread.sleep(500L);
          test_step(step, exp);
          Thread.sleep(1000L);
        }
      }
    }
    driver.findElement(By.xpath("//div[@id='com_ibm_asq_common_web_ui_internal_view_layout_ViewHeaderLayout_1']/div[2]/div/div/button[2]")).click();
    System.out.println("All Test Cases are uploaded!");
  }
  
  public void tearDown() throws Exception
  {
    driver.findElement(By.xpath("//div[@id='com_ibm_asq_common_web_ui_internal_view_layout_ViewHeaderLayout_1']/div[2]/div/div/button[2]")).click();
    Thread.sleep(4000L);
    JOptionPane.showMessageDialog(null, "All Test Cases are uploaded!");
    int confirm = JOptionPane.showConfirmDialog(null, "Do you want to close the browser?", "Thanks For Auto Uploading TCs", 0);
    driver.get(baseUrl + "/qm/web/console/");
    if (confirm == 0)
      driver.quit();
    String verificationErrorString = verificationErrors.toString();
    if (!"".equals(verificationErrorString)) {
      System.out.println("All Test Cases are uploaded!");
    }
  }
  
  public void login(String user, String pass)
  {
    try {
      driver.get(baseUrl);
      driver.findElement(By.id("jazz_app_internal_LoginWidget_0_userId")).sendKeys(new CharSequence[] { user });
      Thread.sleep(500L);
      driver.findElement(By.id("jazz_app_internal_LoginWidget_0_password")).sendKeys(new CharSequence[] { pass });
      Thread.sleep(500L);
      driver.findElement(By.cssSelector("button[type=\"submit\"]")).click();
      Thread.sleep(500L);
    } catch (Exception e) {
      if (driver.findElement(By.id("jazz_app_internal_LoginWidget_0_userId")).isDisplayed()) {
        login(userid, passwd);
      } else
        JOptionPane.showMessageDialog(null, "Login Exception!");
    }
  }
  
  public void summary(String name, String desc, String functionalGroup, String SubFunctionGroup, String Failureimpact, String FailureLikly) {
    try {
      Thread.sleep(3000L);
      driver.findElement(By.id("jazz_ui_MenuPopup_8")).click();
      Thread.sleep(1000L);
      driver.findElement(By.id("jazz_ui_menu_MenuItem_5_text")).click();
      Thread.sleep(1000L);
      
      driver.findElement(By.id("com_ibm_asq_common_web_ui_internal_widgets_TitleTextAreaEditor_0")).sendKeys(new CharSequence[] { name });
      Thread.sleep(1000L);
      driver.findElement(By.id("com_ibm_asq_common_web_ui_internal_view_layout_ViewHeaderLayout_0-summary-text-area")).sendKeys(new CharSequence[] { desc });
      Thread.sleep(1000L);
      
      driver.findElement(By.cssSelector("option[title=\"" + functionalGroup + "\"]")).click();
      Thread.sleep(500L);
      driver.findElement(By.cssSelector("option[title=\"" + SubFunctionGroup + "\"]")).click();
      Thread.sleep(500L);
      driver.findElement(By.cssSelector("option[title=\"" + Failureimpact + "\"]")).click();
      Thread.sleep(500L);
      driver.findElement(By.cssSelector("option[title=\"" + FailureLikly + "\"]")).click();
      writeLogs(TestCaseName + " :: TestCase Title uploaded successfully");
    } catch (Exception e) {
      writeLogs("Summary Error : " + e.getCause() + " Message : " + e.getMessage());
    }
  }
  
  public void description(String desc)
  {
    try {
      Thread.sleep(1000L);
      driver.findElement(By.cssSelector("a[title=\"Test Description\"]")).click();
      Thread.sleep(1000L);
      driver.findElement(By.xpath("(//a[contains(text(),'Add Content')])[1]")).click();
      Thread.sleep(1000L);
      action.sendKeys(new CharSequence[] { desc }).perform();
      delay(desc);
      writeLogs(TestCaseName + " :: Description uploaded successfully");
    } catch (Exception e) {
      writeLogs("Discription Error : " + e.getCause() + " Message : " + e.getMessage());
    }
  }
  
  public void pre_condition(String precond) {
    try {
      Thread.sleep(1000L);
      driver.findElement(By.cssSelector("a[title=\"Pre-Condition\"]")).click();
      Thread.sleep(1000L);
      driver.findElement(By.xpath("(//a[contains(text(),'Add Content')])[2]")).click();
      Thread.sleep(1000L);
      action.sendKeys(new CharSequence[] { precond }).perform();
      delay(precond);
      writeLogs(TestCaseName + " :: Pre condition uploaded successfully");
    } catch (Exception e) {
      writeLogs("Pre condition Error : " + e.getCause() + " Message : " + e.getMessage());
    }
  }
  
  public void post_condition(String postcond) {
    try {
      Thread.sleep(1000L);
      driver.findElement(By.cssSelector("a[title=\"Post-Condition\"]")).click();
      Thread.sleep(1000L);
      driver.findElement(By.xpath("(//a[contains(text(),'Add Content')])[3]")).click();
      Thread.sleep(1000L);
      action.sendKeys(new CharSequence[] { postcond }).perform();
      delay(postcond);
      writeLogs(TestCaseName + " :: Post condition uploaded successfully");
    } catch (Exception e) {
      writeLogs("Post condition Error : " + e.getCause() + " Message : " + e.getMessage());
    }
  }
  
  public void test_script(String name, String desc) {
    try {
      Thread.sleep(1000L);
      driver.findElement(By.cssSelector("a[title=\"Test Scripts\"]")).click();
      Thread.sleep(1000L);
      driver.findElement(By.cssSelector("img.button-img.add-new-testscript-image")).click();
      Thread.sleep(1000L);
      driver.findElement(By.id("com_ibm_asq_common_web_ui_internal_widgets_layout_ASQValidateTextBox_1")).sendKeys(new CharSequence[] { name });
      Thread.sleep(100L);
      driver.findElement(By.id("com_ibm_asq_common_web_ui_internal_widgets_TextareaBidi_0")).sendKeys(new CharSequence[] { desc });
      Thread.sleep(100L);
      driver.findElement(By.cssSelector("span.button-div > button")).click();
      Thread.sleep(1000L);
      driver.findElement(By.xpath(".//*[@id='com_ibm_asq_common_web_ui_internal_view_layout_ViewHeaderLayout_0']/div[2]/div[1]/div[1]/button[2]")).click();
      Thread.sleep(3000L);
      driver.findElement(By.xpath("//table[@summary='This is Test Scripts table']/tbody/tr[1]/td[3]/a[1]")).click();
      Thread.sleep(5000L);
      writeLogs(TestCaseName + " :: Test Script uploaded successfully");
    } catch (Exception e) {
      writeLogs("Test Script Error : " + e.getCause() + " Message : " + e.getMessage());
    }
  }
  
  public void test_step(String step, String exp) throws InterruptedException {
    try {
      Thread.sleep(1000L);
      action.sendKeys(new CharSequence[] { step }).perform();
      Thread.sleep(1000L);
      action.keyDown(Keys.ALT).perform();
      action.sendKeys(new CharSequence[] { Keys.RIGHT }).perform();
      action.keyUp(Keys.ALT).perform();
      Thread.sleep(500L);
      action.sendKeys(new CharSequence[] { exp }).perform();
      Thread.sleep(1000L);
    } catch (Exception e) {
      writeLogs("Test Step Error : " + e.getCause() + " Message : " + e.getMessage());
    }
  }
  
  public void delay(String s) {
    try { Thread.sleep(s.length() * 10);
    }
    catch (InterruptedException e) {
      e.printStackTrace();
    }
  }
  
  public void writeLogs(String sLog) {
    try {
      String sLogString = new SimpleDateFormat("MM-dd-YYYY HH:mm:ss").format(new Date()) + ": " + sLog;
      BufferedWriter oBufferedWriter = new BufferedWriter(new java.io.FileWriter(sLogFileName, true));
      oBufferedWriter.append(sLogString + "\r\n");
      System.out.println(sLogString);
      oBufferedWriter.flush();
      oBufferedWriter.close();
    } catch (Exception e) {
      System.out.println(e.getMessage());
    }
  }
}
