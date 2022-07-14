medida = float(input('Uma distância em metros: '))
mm = medida * 1000
cm = medida * 100
dm = medida * 10
dam = medida * 0.1
hm = medida * 0.01
km = medida * 0.001
print('A medida de {}m corresponde a \n {:.0f}mm \n {:.0f}cm \n {:.0f}dm \n {:.1f}dam \n {:.2f}hm \n {:.3f}km.'.format(medida, mm, cm, dm, dam, hm, km))

