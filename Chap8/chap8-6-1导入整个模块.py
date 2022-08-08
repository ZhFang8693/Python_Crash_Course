# 导入模块

# 模块:是指扩展名为.py的文件.模块中的函数即该文件中所包含的函数
# 导入模块中所有函数时,不需要加后缀
import Chap9.pizza as pizza
# pizza.makepizza()这里是标准格式,前面是模块名称,后面是函数名称,当仅仅导入了模块
# 时,需要同时指定模块名称和函数名称
pizza.make_pizza(9,'pepperoni')
pizza.make_pizza(12,'pepperoni','cheese','beef')

# 导入模块中特定函数时,可以指定函数,格式如下:
from Chap9.pizza import make_pizza

pizza.make_pizza(9,'pepperoni')
pizza.make_pizza(12,'pepperoni','cheese','beef')

# 当觉得函数名太长时,可以给函数指定别名
# 这里的mp指代的是form pizza import make_pizza:
from Chap9.pizza import make_pizza as mp
# 此时可以使用mp指代该模块下的该函数,因此不需要带模块名称
mp(9,'pepperoni')

# 除函数名外,也可以给模块指定别名,格式为:
import Chap9.pizza as pi
# 这里是重新导入,因此mp在此不可用.需要重新输入全名make_pizza
# 且,由于只import了模块,因此需要标准格式,即模块+函数:
# 这里省略模块名,可以使代码阅读者专注于阅读解释性的函数名,让代码更方便阅读
pi.make_pizza(9,'pepperoni')


# *表示导入该模块下所有函数,但是非到必要时不要使用它,因为:
# 导入的函数中如果有函数名和项目中使用的名称相同,会导致莫名其妙的错误
# 很多时候会遇到命名相同的函数,这时候就会覆盖函数,导致错误
from Chap9.pizza import *