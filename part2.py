
# დავალება 4
# მომხმარებელს შემოჰყავს რიცხვები თითო გამოტოვებით, (ულიმიტოდ რამდენიც უნდა) პროგრამა
# სთავაზობს როგორ უნდა რომ დაუსორტირდეს აღნიშნული: კლებადობით, ზრდადობით, random-ად ან
# მხოლოდ უნიკალური მონაცემები დატოვოს. რომელსაც აირჩევს უნდა გამოვიდეს ზუსტად ისე
# დალაგებული სია.
lst = []
i = 0
print('კლავიატურის გამოყენებით შემოიტანეთ რამდენიმე მნიშვნელობა')
while i < 10:
    numb = int(input())
    lst.append(numb)
    i += 1


lst_acc = sorted(lst)
lst_des = sorted(lst, reverse=True)
lst_unic = sorted(set(lst))

print(f'lst: {lst}\nlst_acc:{lst_acc}\nlst_des: {lst_des}\nlst_unic: {lst_unic}')





#  დავალება 5 #5 ტექსტის ფილტრი
# მომხმარებელი შეჰყავს ტექსტი.
# ამოცანა: პროგრამამ უნდა წაშალოს ყველა ციფრი და სიმბოლო, დატოვოს მხოლოდ ასოები და
# სივრცეები.


text = input("შეიყვანეთ ტექსტი: ")
filtered_text = ''.join(char for char in text if char.isalpha() or char.isspace())
print("ფილტრის შედეგი:", filtered_text)








# დავალება 6
# მომხმარებელს შეჰყავს რიცხვების სია (მაგ. 3,5,7,2).
# ამოცანა: შექმენი “პირამიდა”, სადაც ყოველი ახალი რიგი ზემოთაა წინა ორი რიცხვის ჯამი.

def mypiramid (nums):
    mypiramid = [nums]
    while len(mypiramid) > 1:
        nums = [nums[1]+ nums [i+1] for i in range (len(nums)-1)]
        mypiramid.append(nums)
        return mypiramid
    else:
        return mypiramid[0]
    nums = input("შემოიტანე რიცხვები: 3,5,7,2")
    nums = [int(x) for x in nums.split(",")]
