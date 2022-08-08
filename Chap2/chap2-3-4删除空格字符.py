## chap2-3-4删除空格字符

fav_language = '   Python   '
print (fav_language)

## 要删除行末空格字符,用到的是rstrip()方法
print (fav_language.rstrip())

## 删除行头空格,用到的是lstrip()方法
print (fav_language.lstrip())

## 删除两端空格,用到的是strip()方法
print (fav_language.strip())