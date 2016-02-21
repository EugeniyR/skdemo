# This is a demo skript to display the feature of sikuli

import os


# ============ constants ==================
homePageUrl = "http://www.epam.com"


# ============ images =====================
# ainol specific
LTainol = "lt_ainol.png"
browser = "browser.png"
sixDots = "sixDots.png"
browserHome = "browserHome.png"

# home page images
mobileMenu = "mobileMenu.png"
topUtilityMenu = "topUtilityMenu.png"
learnMoreBtn  = "learnMoreBtn.png"
whatsNewBtn   = "whatsNewBtn.png"
whoWeAre_1   = "whoWeAre_1.png"
whoWeServe_0 = "whoWeServe_0.png"
whatWeDo_0   = "whatWeDo_0.png"
developers   = "developers.png"
testers      = "testers.png"
designers    = "designers.png"
solutionExperts = "solutionExperts.png"
deliveryMngr = "deliveryMngr.png"
leaders      = "leaders.png"
whatsNew     = "whatsNew.png"
theLatest_1  = "theLatest_1.png"
pressReleases_0 = "pressReleases_0.png"
events_0     = "events_0.png"
inTheNews_0  = "inTheNews_0.png"
viewAllBtn   = "viewAllBtn.png"
contactUsBtn = "contactUsBtn.png"
leftFooter   = "leftFooter.png"
middleFooter = "middleFooter.png"
rightFooter  = "rightFooter.png"






# ============= scripts ====================
def verifyHomePage(pageUrl):
    # check the page structure
    # outputs the test results
    # returns string with the summary of test results
    result = True
    # perform the tests
    browserAddress = Region(find(browserHome)).right()
    paste(browserAddress, pageUrl)
    wait(1)
    type(Key.ENTER)
    print "Browser address string found." 
    # wait until the change in the middle of the page (TBD)
    wait(10)

    # verify the top menu
    topLeft = browserAddress.below(100).left()
    if (not topLeft.exists(mobileMenu)):
        print "Mobile menu not found. - Failed"
        result = False
    else: 
        print "Mobile menu found. - Passed"
        topLeft = Region(find(mobileMenu))
        if (not topLeft.right().exists(topUtilityMenu)):
            result = False
            print "Top Utility Menu not found. - Failed"
        else:
            print "Top Utility Menu found."
        
    # verify the text
    block1Text = text()
    print block1Text
    
    # verify the two buttons (TBD)
    wheel(learnMoreBtn, WHEEL_DOWN, 1)
    wait(2)
    if (not exists(learnMoreBtn)):
        print "Learn More Button not found. - Failed"
        result = False
    else: 
        print "Learn More Button found. - Passed"
            
    
    print "verifyHomePage : \r\n" + str(result)
    return result
# end of def verifyHomePage(pageUrl):


def startBrowser(home, browser):
    # click the home image, search for browser and start it
    if (not exists(home)):
        result = "sixDots not found. \r\n"
    else:
        click(home)
        waitVanish(home)        
        result = "sixDots found. \r\n"
    
    wait(1)
    click(browser)
    waitVanish(browser)

    print "startBrowser : " + result
    return result

# ============= settings ===================
myPath = os.path.dirname(getBundlePath())
print (myPath )
#selectDevice()
imgPath = myPath + "\\epam.sikuli\\imgs\\ainol"
addImagePath (imgPath)
print ("The real image path is: " + imgPath)
#"E:\\skdemo\\epam.sikuli\\imgs\\ainol"

# We can check the speed and use it later on
#startTime = 
startBrowser(sixDots, browser)
#stopTime = 
#elapsedTime = 

# ============= test cases ================

verifyHomePage(homePageUrl)