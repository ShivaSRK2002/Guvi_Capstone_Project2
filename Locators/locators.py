file_path = "/Users/dilipkumar.g/PycharmProjects/pythonProject1/DataDrivenFramework/Data/login_creds.xls"
login_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
home_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
main_menu = ["Admin","PIM","Leave","Time","Recruitment"]
side_panel = ["User Management","Job","Organization","Qualifications","Nationalities","Corporate Branding","Configuration"]
xpaths_main_menu = ["//span[text()='Admin']","//span[text()='PIM']","//span[text()='Leave']","//span[text()='Time']","//span[text()='Recruitment']"]
xpath_admin_page = ["//span[text()='User Management ']","//span[text()='Job ']","//span[text()='Organization ']",
                  "//span[text()='Qualifications ']","//a[text()='Nationalities']","//a[text()='Corporate Branding']","//span[text()='Configuration ']"]

class LoginLocators:
    username_element = "//input[@name='username']"
    password_element = "//input[@name='password']"
    submit_element = "//button[@type='submit']"
    profile_button_element = "//span[@class='oxd-userdropdown-tab']"
    logout_button_element = "//a[text()='Logout']"
    valid_username = "Admin"
    valid_password = "admin123"
    admin = "//span[text()='Admin']"
    title = "//title[text()='OrangeHRM']"
    forgot_password = "//p[text()='Forgot your password? ']"
    username_text_box = "//input[@name='username']"
    reset_password = "//button[text()=' Reset Password ']"
    header_6 = "//h6"