def replace_exclamation(s):
   
    print( ''.join('!' if c in 'aeiouAEIOU' else c for c in s))

replace_exclamation('give me my APPLE !')
#g!v! m! my !PPL! !
#this code will change all vowels(aeiouAEIOU) in the dictionary to !