from pylayers.antprop.coverage import *
C = Coverage()
C.cover(polar='o')
f,a = C.show(typ='pr')
plt.show()
f,a = C.show(typ='best')
plt.show()
f,a = C.show(typ='loss')
plt.show()
f,a = C.show(typ='sinr')
plt.show()