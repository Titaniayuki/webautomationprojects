
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep



def main():
    #ask what you want
   
    #task = int(input("what do you want to do?\nquestrade -1\n"))
    questrade()
    #if (task == 1):
    #    questrade()
    #else:
    #    pass


    #ask username
    #ask password
    #give results
    return()


def questrade():

    done = False


    driverforquestrade = webdriver.Chrome()
    driverforquestrade.get('https://www.questrade.com/home')

    
    login = driverforquestrade.find_element_by_xpath('/html/body/header/div[1]/div[1]/a[2]')
  
    

    while (not done):

        

        login.click()
        
        UserID = driverforquestrade.find_element_by_xpath('//*[@id="userId"]')
        UserID.send_keys(USERNAME)


        passwordentry = driverforquestrade.find_element_by_xpath('//*[@id="password"]')
        passwordentry.send_keys(PASSWORD)

        loginbutton = driverforquestrade.find_element_by_xpath('/html/body/div[2]/div[1]/form/div[3]/button')
        loginbutton.click()

        #confirm login by checking if there is a send code button
        button = driverforquestrade.find_element_by_name ('button')
        buttontext = button.text

        if (buttontext == 'Send Code'):
            #login failed
            print("log in failed/n")
        else:
            sleep(3)
            emailcode = driverforquestrade.find_element_by_xpath('/html/body/div[2]/div/form/div[3]/label')
            emailcode.click()

            ###########
            button.click()


            #retrieve code
            code = getcode()
                                  
            entercode = driverforquestrade.find_element_by_xpath('//*[@id="Code"]')
            entercode.send_keys(code)

            verify = driverforquestrade.find_element_by_xpath('//*[@id="btn-verify"]')
            verify.click()

            #confirm pass
            
            pagetitle = driverforquestrade.find_element_by_xpath('/html/body/app-root/div/app-myqhome/myq-summary/div/div/div[1]/myq-balance/div/div[1]')
            if (pagetitle != None):
                #in
                getdata(driverforquestrade)
            else:
                #code didn't work
                print("invalid code")

        done = True
        
    return()

def getdata(driverforquestrade):
    #trade =  driverforquestrade.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[5]/button')
    #trade.click()
    
    #sleep(20)
    #selectbox = Select(driverforquestrade.find_element_by_xpath('/html/body/main/div[3]/header/div[2]/div/div/div/select'))
    #print (selectbox.options)
    #print [o.text for o in select.options] # these are string-s
    #select.select_by_visible_text(....)

    #TFSA=selectbox.select_by_index(0)

    #TFSATOTAL = driverforquestrade.find_element_by_xpath('/html/body/main/div[5]/div/div/div/div[2]/div/div/div/div[3]/div/table/tbody[1]/tr[1]/td[4]/iq-format-number/span').text
    #print('TFSA total: %s ' % TFSATOTAL)

    #TFSA=selectbox.select_by_index(1)
    #RRSPTOTAL = driverforquestrade.find_element_by_xpath('/html/body/main/div[5]/div/div/div/div[2]/div/div/div/div[3]/div/table/tbody[1]/tr[1]/td[4]/iq-format-number/span').text
    #print('RRSP total: %s ' % RRSPTOTAL)
    
    sleep(5)
    RRSPTOTAL = driverforquestrade.find_element_by_xpath('/html/body/app-root/div/app-myqhome/myq-active-accounts/div/div/div[1]/div/div[4]/p/span').text
    print('RRSP total: %s ' % RRSPTOTAL)
    TFSATOTAL = driverforquestrade.find_element_by_xpath('/html/body/app-root/div/app-myqhome/myq-active-accounts/div/div/div[2]/div/div[4]/p/span').text
    print('TFSA total: %s ' % TFSATOTAL)

    return()

def getcode():

    done = False

    driverforoutlook = webdriver.Chrome()
    driverforoutlook.get('https://outlook.live.com/owa/0/?state=1&redirectTo=aHR0cHM6Ly9vdXRsb29rLmxpdmUuY29tL21haWwvMC9pbmJveA')

    gotosignin = driverforoutlook.find_element_by_xpath('/html/body/header/div/aside/div/nav/ul/li[2]/a')
    gotosignin.click()


    #email = input("email")
    

    emailentry = driverforoutlook.find_element_by_xpath('//*[@id="i0116"]')
    emailentry.send_keys(EMAIL)

    next = driverforoutlook.find_element_by_xpath('//*[@id="idSIButton9"]')
    next.click()

    #password = input("Password?")
    passwordentry = driverforoutlook.find_element_by_xpath('//*[@id="i0118"]')
    passwordentry.send_keys(EMAILPASSWORD)
    
    sleep(3)

    signin = driverforoutlook.find_element_by_xpath('//*[@id="idSIButton9"]')
    signin.click()

    emails = driverforoutlook.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[1]/div/div/div[3]/div[2]/div/div[1]/div[2]/div/div/div/div/div/div[1]')
    stringcheck = emails.text
    
    code = 'unknown'
    if("Questrade No-Reply" in stringcheck):
        #got email 
        prevword = 'temp' 
        
            #get code
                
        for word in stringcheck.split():
            if (prevword == 'account:'):
                code = word
                break
            else:
                prevword = word
    return(code)

main()