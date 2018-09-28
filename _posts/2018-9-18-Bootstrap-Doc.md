576px		Extra-small	.col-	
>575px		Small		.col-sm-
>768px		Medium		.col-md-
>992px		Large		.col-lg-
>1200px		Extra-large	.col-xl-
全都使用col类时会自动均分div宽度
可以使用w-100类来划分出不同的行（Safari可能会有问题）
w-100类其实就是设定了一个宽度为100（高度为0）的块，来让其他块自动分配到下一行
设定一个col的宽度如（col-6），其他就会自动均分剩余宽度
可以使用col-{breakpoint}-auto来设定一个根据文本自适应宽度的div

响应式类
如果不是有根据屏幕大小设定的特殊需要，对于各种尺寸的屏幕都可以使用col和col-n类
使用两个row类叠加，就可以划分出有间距的两行div
如果希望在不同情况下出现不同的堆叠方式，就可以将多个col类写进容易个class attr，例如："col-6 col-md-4"

对齐
垂直对齐：
如果希望只占高度的一部分，但是都在同一垂直线上，就可以在row中使用
align-items-start
align-items-center
align-items-end
或者在不同的col中使用
align-self-start
align-self-center
align-self-end

水平对齐
在row中使用
justify-content-start靠左
justify-content-center中间
justify-content-end靠右
justify-content-around空白宽度分配到各个块之间（最靠两边的是空白）
justify-content-between空白宽度集中到块之间（最靠两边的是块）

去除边框
no-gutters:去除col之间的左右边框margin和上下的边框padding

如果一行的宽度超过12个单位，超出的单位就会自动被放到新的一行


重排序/////////////////////
同一行内所有设定了order-相关的块会进行一次重排序，例如
order-1的块会被放到order-12前面

块偏移
使用offset可以将块偏移一定宽度
这种方式实际上是通过增加左侧margin来实现的
例如"col-md-4 offset-md-4"
如果你的class里有多个对应的宽度类，如col，col-md那你也需要就每个类来设定相对应的offset
https://v4.bootcss.com/docs/4.0/layout/grid/#margin-utilities
