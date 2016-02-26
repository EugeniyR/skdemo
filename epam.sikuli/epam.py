# This is a demo skript to display the features of SikuliX.
# Team Viewer is used to control the real Android device.

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
threeTabs    = "threeTabs.png"
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
fourTabs     = "fourTabs.png"
iconPaper    = "iconPaper.png"
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
    browserAddress = Region(find(browserHome)).right(800)
    browserAddress.highlight(1)
    paste(browserAddress, pageUrl)
    #type(browserAddress, pageUrl + Key.ENTER)
    wait(2)
    type(Key.ENTER)
    print "Browser address string found." 
    # wait until the change in the middle of the page (TBD)
    wait(mobileMenu, 15)
    wait(2)
    #tmmr = Region(getLastMatch())
    #tmmr.highlight(2)

    # verify the top menu
    topLeft = browserAddress.below(100).left()
    if (not topLeft.exists(mobileMenu)):
        print "Mobile menu not found. - Failed"
        result = False
    else: 
        print "Mobile menu found. - Passed"
        topLeft = Region(find(mobileMenu))
        topLeft.highlight(1)
        if (not topLeft.right().exists(topUtilityMenu)):
            result = False
            print "Top Utility Menu not found. - Failed"
        else:
            print "Top Utility Menu found. - Passed"
            utmr = Region(topLeft.right().find(topUtilityMenu))
            utmr.highlight(1)
        
    # verify the text
    appRegion = topLeft.below(370).right(980)
    appRegion.highlight(1)
    #block1Text = appRegion.text().encode('utf-8')
    #print "Block1 text: " + block1Text
    
    # verify Learn More Button & What's New Button
    #wheel(learnMoreBtn, WHEEL_DOWN, 1)
    appRegion.hover()
    wait(1)
    while (not appRegion.exists(learnMoreBtn)):
        wheel(WHEEL_DOWN, 1)
        wait(1)
    if (not appRegion.exists(learnMoreBtn)):
        print "Learn More Button not found. - Failed"
        result = False
    else: 
        print "Learn More Button found. - Passed"
        lmbr = Region(appRegion.find(learnMoreBtn))
        lmbr.highlight(1)
        # verify What's New Button is displayed
        if (not lmbr.right().exists(whatsNewBtn)):
            print "What's New Button not found. - Failed"
            result = False
        else: 
            print "What's New Button found. - Passed"
            wnbr = lmbr.right().find(whatsNewBtn)
            wnbr.highlight(1)
            
    # verify 3 tabs are displayed (TBD)
    wait(1)
    wheel(WHEEL_DOWN, 1) # just do it
    wait(1)
    # temporary consolidated solution
    while (not appRegion.exists(threeTabs)):
        wheel(WHEEL_DOWN, 1)
        wait(1)
    if (not appRegion.exists(threeTabs)):
        print "Three tabs not found. - Failed"
        result = False
    else: 
        print "Three tabs found. - Passed"
        wwar = Region(appRegion.find(threeTabs))
        wwar.highlight(1)
        
    # verify six specializaion
    wait(1)
    while (not appRegion.exists(developers)):
        wheel(WHEEL_DOWN, 1)
        wait(1)
    if (not appRegion.exists(developers)):
        print "Developers not found. - Failed"
        result = False
    else: 
        print "Developers found. - Passed"
        devr = Region(appRegion.find(developers))
        devr.highlight(1)
    if (not appRegion.exists(testers)):
        print "Testers not found. - Failed"
        result = False
    else: 
        print "Testers found. - Passed"
        tesr = Region(appRegion.find(testers))
        tesr.highlight(1)

    # Designers & Solution Experts 
    wait(1)
    while (not appRegion.exists(designers)):
        wheel(WHEEL_DOWN, 1)
        wait(1)
    if (not appRegion.exists(designers)):
        print "Developers not found. - Failed"
        result = False
    else: 
        print "Developers found. - Passed"
        desr = Region(appRegion.find(designers))
        desr.highlight(1)
    if (not appRegion.exists(solutionExperts)):
        print "Solution Experts not found. - Failed"
        result = False
    else: 
        print "Solution Experts found. - Passed"
        tesr = Region(appRegion.find(solutionExperts))
        tesr.highlight(1)
    
    # Delivery Managers & Leadres                    
    wait(1)
    while (not appRegion.exists(deliveryMngr)):
        wheel(WHEEL_DOWN, 1)
        wait(1)
    if (not appRegion.exists(deliveryMngr)):
        print "Delivery Managers not found. - Failed"
        result = False
    else: 
        print "Delivery Managers found. - Passed"
        dlmr = Region(appRegion.find(deliveryMngr))
        dlmr.highlight(1)
    if (not appRegion.exists(leaders)):
        print "Leadres not found. - Failed"
        result = False
    else: 
        print "Leadres found. - Passed"
        ldrr = Region(appRegion.find(leaders))
        ldrr.highlight(1)
                        

    # verify 4 tabs are displayed
    # Temporary
    wait(1)
    while (not appRegion.exists(fourTabs)):
        wheel(WHEEL_DOWN, 1)
        wait(1)
    if (not appRegion.exists(fourTabs)):
        print "Delivery Managers not found. - Failed"
        result = False
    else: 
        print "Delivery Managers found. - Passed"
        ftbr = Region(appRegion.find(fourTabs))
        ftbr.highlight(1)
    
    # drag and drop the carousel
    t1 = appRegion.get(Region.EAST).find(iconPaper)
    #dragDrop(t1, [t1.x - 450, t1.y])
    dragDrop(t1, t1.offset(Location(-450, 0)))
    wait(2)
    t1 = appRegion.get(Region.EAST).find(iconPaper)
    dragDrop(t1, [t1.x - 450, t1.y])
    wait(2)
    ppr = get(Region.WEST)
    t1 = appRegion.get(Region.EAST).find(iconPaper)
    dragDrop(t1, [t1.x + 450, t1.y])
    wait(2)
    
    # verify View All button is present    
    wait(1)
    while (not appRegion.exists(viewAllBtn)):
        wheel(WHEEL_DOWN, 1)
        wait(1)
    if (not appRegion.exists(viewAllBtn)):
        print "Delivery Managers not found. - Failed"
        result = False
    else: 
        print "Delivery Managers found. - Passed"
        ftbr = Region(appRegion.find(viewAllBtn))
        ftbr.highlight(1)


    
    # verify the spin ribbon is displayed
    # verify ContactUs button is present
    # verify ContactUs button and the bottom menu is displayed
    appRegion.hover()
    wait(1)
    while (not appRegion.exists(middleFooter)):
        wheel(WHEEL_DOWN, 1)
        wait(1)

    # verify ContactUs button is present
    if (not appRegion.exists(contactUsBtn)):
        print "Contact Us Button not found. - Failed"
        result = False
    else: 
        print "Contact Us Button found. - Passed"
        cubr = Region(appRegion.find(contactUsBtn))
        cubr.highlight(1)
    
    # verify the bottom menu is displayed
    wait(1)
    if (not appRegion.exists(middleFooter)):
        print "Middle Footer not found. - Failed"
        result = False
    else: 
        print "Middle Footer found. - Passed"
        mfr = Region(appRegion.find(middleFooter))
        mfr.highlight(1) 
        
    # verify Left Footer is displayed
    #if (not appRegion.exists(leftFooter)):
    if (not mfr.left().exists(leftFooter)):
        print "Left Footer not found. - Failed"
        result = False
    else: 
        print "Left Footer found. - Passed"
        lfr = Region(mfr.left().find(leftFooter))
        lfr.highlight(1)        
        
    # verify Right Footer is displayed
    if (not appRegion.exists(rightFooter)):
    #if (not mfr.right().exists(rightFooter)):
        print "Right Footer not found. - Failed"
        result = False
    else: 
        print "Right Footer found. - Passed"
        #rfr = Region(mfr.right().find(rightFooter))
        rfr = Region(appRegion.find(rightFooter))
        rfr.highlight(1)
            
    
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