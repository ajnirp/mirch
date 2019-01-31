import math
import naoqi

nav = naoqi.ALProxy('ALNavigation', "152.23.151.210", 9559)
motion = naoqi.ALProxy('ALMotion', "152.23.151.210", 9559)

# nav.moveAlong(["Composed", ["Holonomic", ["Line", [0.3, 0.3]], 45*math.pi/180.0, 2.0], ["Holonomic", ["Line", [0.3, 0.5]], math.atan(5.0/3.0), 3.0], ["Holonomic", ["Line", [0.3, -0.5]], -math.atan(5.0/3.0), 3.0]])

# nav.moveAlong(["Composed", ['NonHolonomic', ['Composed', ["Line", [0.3, 0]], ["Line", [0.3, 0]]], 2]])
# nav.moveAlong(["Composed", ["Holonomic", ["Line", [0.3, 0]], 0, 0.6], ['Holonomic', ["Line", [0.3, 0]], 0, 0.6]])

# nav.moveAlong(["Composed", ["NonHolonomic", ["Composed", ["Line", [0.2, 0]], ["Line", [0.3, 0.2]], ["Line", [0.4, 0]]], 2]]) # <-------------

# nav.moveAlong(["Composed", ["NonHolonomic", ["Composed", ["Circle", [0.000000021, -0.474395216], -1.216920137], ["Circle", [0.222957313, 0.082366571], 3.769504786], ["Circle", [0.139780164, 0.209214211], -1.939481378], ["Circle", [-0.187792718, 0.266922235], 3.387900829], ["Circle", [-4.597937107, 3.963142157], -0.102580860], ["Circle", [0.162999302, -0.172588766], 2.027587891], ["Line", [0.000000000, 0.000000000]]], 16]])

nav.moveAlong(['Composed', ['NonHolonomic', ['Composed', ['Line', [0.022348, 0.002652]], ['Line', [0.022086, 0.002881]], ['Line', [0.021826, 0.003102]], ['Line', [0.021572, 0.003316]], ['Line', [0.021322, 0.003522]], ['Line', [0.021075, 0.00372]], ['Line', [0.020831, 0.003911]], ['Line', [0.020592, 0.004094]], ['Line', [0.020355, 0.00427]], ['Line', [0.020122, 0.004439]], ['Line', [0.019892, 0.004601]], ['Line', [0.019665, 0.004756]], ['Line', [0.019441, 0.004904]], ['Line', [0.019218, 0.005046]], ['Line', [0.018999, 0.005181]], ['Line', [0.018783, 0.005309]], ['Line', [0.018567, 0.005431]], ['Line', [0.018355, 0.005547]], ['Line', [0.018145, 0.005657]], ['Line', [0.017935, 0.00576]], ['Line', [0.017729, 0.005858]], ['Line', [0.017524, 0.005949]], ['Line', [0.01732, 0.006035]], ['Line', [0.017117, 0.006115]], ['Line', [0.016917, 0.006189]], ['Line', [0.016717, 0.006258]], ['Line', [0.016519, 0.006321]], ['Line', [0.016322, 0.006378]], ['Line', [0.016125, 0.006431]], ['Line', [0.01593, 0.006478]], ['Line', [0.015735, 0.006519]], ['Line', [0.015541, 0.006556]], ['Line', [0.015349, 0.006588]], ['Line', [0.015156, 0.006614]], ['Line', [0.014964, 0.006636]], ['Line', [0.014773, 0.006653]], ['Line', [0.014581, 0.006665]], ['Line', [0.014392, 0.006672]], ['Line', [0.014202, 0.006676]], ['Line', [0.014011, 0.006674]], ['Line', [0.013823, 0.006668]], ['Line', [0.013634, 0.006658]], ['Line', [0.013445, 0.006644]], ['Line', [0.013256, 0.006625]], ['Line', [0.013069, 0.006603]], ['Line', [0.01288, 0.006577]], ['Line', [0.012693, 0.006547]], ['Line', [0.012506, 0.006513]], ['Line', [0.012319, 0.006476]], ['Line', [0.012132, 0.006435]], ['Line', [0.011945, 0.006392]], ['Line', [0.01176, 0.006344]], ['Line', [0.011574, 0.006294]], ['Line', [0.011389, 0.006241]], ['Line', [0.011204, 0.006185]], ['Line', [0.01102, 0.006126]], ['Line', [0.010836, 0.006065]], ['Line', [0.010653, 0.006002]], ['Line', [0.010471, 0.005935]], ['Line', [0.01029, 0.005867]], ['Line', [0.010109, 0.005797]], ['Line', [0.009929, 0.005725]], ['Line', [0.00975, 0.005651]], ['Line', [0.009572, 0.005575]], ['Line', [0.009395, 0.005498]], ['Line', [0.009219, 0.00542]], ['Line', [0.009044, 0.00534]], ['Line', [0.008871, 0.005259]], ['Line', [0.008699, 0.005178]], ['Line', [0.008528, 0.005094]], ['Line', [0.008358, 0.005011]], ['Line', [0.008191, 0.004927]], ['Line', [0.008122, 0.00494]], ['Line', [0.008769, 0.005583]], ['Line', [0.01171, 0.007293]], ['Line', [0.011504, 0.007165]], ['Line', [0.0113, 0.007038]], ['Line', [0.011092, 0.006909]], ['Line', [0.010886, 0.00678]], ['Line', [0.010679, 0.00665]], ['Line', [0.010471, 0.006522]], ['Line', [0.010264, 0.006393]], ['Line', [0.010056, 0.006263]], ['Line', [0.009851, 0.006135]], ['Line', [0.009644, 0.006007]], ['Line', [0.00944, 0.005879]], ['Line', [0.009236, 0.005753]], ['Line', [0.009033, 0.005626]], ['Line', [0.008833, 0.005501]], ['Line', [0.008633, 0.005377]], ['Line', [0.008436, 0.005254]], ['Line', [0.00824, 0.005132]], ['Line', [0.008047, 0.005012]], ['Line', [0.007856, 0.004893]], ['Line', [0.007667, 0.004775]], ['Line', [0.007481, 0.004659]], ['Line', [0.007297, 0.004545]], ['Line', [0.007116, 0.004432]], ['Line', [0.006937, 0.004321]], ['Line', [0.006763, 0.004212]], ['Line', [0.00659, 0.004104]], ['Line', [0.006421, 0.003999]], ['Line', [0.006254, 0.003896]], ['Line', [0.006091, 0.003793]], ['Line', [0.005931, 0.003694]], ['Line', [0.005774, 0.003596]], ['Line', [0.00562, 0.003501]], ['Line', [0.00547, 0.003406]], ['Line', [0.005322, 0.003315]], ['Line', [0.005178, 0.003225]], ['Line', [0.005036, 0.003137]], ['Line', [0.004899, 0.003051]], ['Line', [0.004764, 0.002967]], ['Line', [0.004632, 0.002885]], ['Line', [0.004504, 0.002805]], ['Line', [0.004378, 0.002726]], ['Line', [0.004255, 0.002651]], ['Line', [0.004137, 0.002576]], ['Line', [0.004019, 0.002504]], ['Line', [0.004855, 0.002759]], ['Line', [0.005547, 0.002906]], ['Line', [0.006602, 0.003055]], ['Line', [0.007612, 0.00309]], ['Line', [0.008953, 0.003006]], ['Line', [0.010316, 0.002741]], ['Line', [0.011955, 0.002196]], ['Line', [0.013611, 0.001334]], ['Line', [0.015393, -9e-06]], ['Line', [0.017035, -0.001835]], ['Line', [0.01847, -0.004301]], ['Line', [0.019387, -0.007293]], ['Line', [0.019564, -0.010804]], ['Line', [0.018755, -0.014473]], ['Line', [0.016805, -0.018001]], ['Line', [0.013823, -0.020828]], ['Line', [0.01352, -0.021028]], ['Line', [0.01352, -0.021029]], ['Line', [0.013521, -0.021028]], ['Line', [0.01352, -0.021029]], ['Line', [0.01352, -0.021029]], ['Line', [0.01352, -0.021028]], ['Line', [0.013521, -0.021029]], ['Line', [0.01352, -0.021028]], ['Line', [0.01352, -0.021029]], ['Line', [0.01352, -0.021029]], ['Line', [0.013521, -0.021028]], ['Line', [0.01352, -0.021029]], ['Line', [0.01352, -0.021029]], ['Line', [0.01352, -0.021028]], ['Line', [0.013521, -0.021029]], ['Line', [0.01352, -0.021028]], ['Line', [0.01352, -0.021029]], ['Line', [0.01352, -0.021029]], ['Line', [0.013521, -0.021028]], ['Line', [0.01352, -0.021029]], ['Line', [0.01352, -0.021028]]], 10]])