def sum67(nums):
  summ = 0;
  flag = False
  for i in range(0, len(nums)):
    if flag == False :
      if nums[i] == 6 :
        flag = True;
      else : summ += nums[i]
    else :
      if nums[i] == 7: flag = False
  return summ;