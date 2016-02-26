        # verify What We Do tab is displayed
        if (not wwar.right().exists(whatWeDo_0)):
            print "What We Do tab not found. - Failed"
            result = False
        else: 
            print "What We Do tab found. - Passed"
            wwdr = Region(wwar.right().find(whatWeDo_0))
            wwdr.highlight(1)

        # verify Who We Serve tab is displayed
        if (not wwar.right().exists(whoWeServe_0)):
            print "Who We Serve tab not found. - Failed"
            result = False
        else: 
            print "Who We Serve tab found. - Passed"
            wwdr = Region(wwar.right().find(whoWeServe_0))
            wwdr.highlight(1)                   
    
