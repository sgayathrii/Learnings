def end_other(str1, str2):
    if(str1.lower().endswith(str2.lower()) or str2.lower().endswith(str1.lower())):
        return True
    else:
        return False 

print(end_other('AbC', 'HiaBc'))
print(end_other('Hiabc', 'abc'))
print(end_other('abc', 'abXabc'))