'''
Testing for all possible iterations of the competition/submission lifecycle. 
'''


#Test Suite 1 (Parameters as Intended)
'''
#Admin Commands
!crc "cyberpunk" "Chill Cyberpunk Beat Battle" "Here is a description. **Here is some bold stuff**. Here is a link: https://youtube.com."
!crc "dubstep" "Dark Dubstep Beat Battle" "Very long description. Very long description. Very long description. Very long description. Very long description. Very long description. Very long description. Very long description. Very long description. Very long description. Very long description. Very long description."
!crc "cyberpunk" "should return error" "should return error"

!pc "cyberpunk" #bot_testing2
!pc "dubstep" #bot_testing2
!pc "should_return_error" #bot_testing2

!cc "cyberpunk"
!rc "cyberpunk"
!cc "dubstep"
!cc "should_return_error"


#Member Commands (With s, random audio file is submitted)
!s "cyberpunk" "Wretched" "Heavy synth guitar with nice arpeggiations :)"
!s "cyberpunk" "Dune" "Not cyberpunk but just wanted to submit something for the sake of it."
!s "should_return_error" "should_return_error" "should_return_error"
!s "dubstep" "should_return_error_as_dubstep_comp_is_closed" "error"
!us "cyberpunk" 
!us "dubstep" #should return error

!rs "cyberpunk" #bot_testing2
!rs "should_return_error" #bot_testing2
'''


#Test Suite 2 (Invalid Parameters)
'''

'''
