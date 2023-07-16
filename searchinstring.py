

input_string = "dsvbnjkxchnuinrjnheloojknsdkvnudifkhellovndfk"

search_pattern = "hello"

def search_in_string(haystack, needle):
   print("looking for " + needle + " in " + haystack)

   found_the_thing = False
   needle_completion = 0

   for current_letter_position in range(len(haystack)):
      current_letter = haystack[current_letter_position]
      if current_letter == needle[needle_completion]:
         needle_completion+=1
         found_the_thing = True
         if needle_completion == len(needle)-1:
            return current_letter_position
      
      else:
         #we found the wrong letter
         found_the_thing = False
         needle_completion = 0


   if not found_the_thing:
      raise ValueError("No needle " + needle + " found.")
   
result =search_in_string(haystack=input_string, needle=search_pattern)
print(result)
