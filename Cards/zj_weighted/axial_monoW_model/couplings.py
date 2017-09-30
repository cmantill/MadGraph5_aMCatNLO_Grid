# This file was automatically created by FeynRules 2.0.28
# Mathematica version: 9.0 for Linux x86 (64-bit) (February 7, 2013)
# Date: Tue 7 Oct 2014 18:10:49


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-(ee*complex(0,1))/3.',
                order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_5 = Coupling(name = 'GC_5',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_6 = Coupling(name = 'GC_6',
                value = '-G',
                order = {'QCD':1})

GC_7 = Coupling(name = 'GC_7',
                value = 'complex(0,1)*G',
                order = {'QCD':1})

GC_8 = Coupling(name = 'GC_8',
                value = 'complex(0,1)*G**2',
                order = {'QCD':2})

GC_9 = Coupling(name = 'GC_9',
                value = '(Cp*complex(0,1)*g1p)/3.',
                order = {'QED':1})

GC_10 = Coupling(name = 'GC_10',
                 value = '-(Cp*complex(0,1)*g1p)',
                 order = {'QED':1})

GC_11 = Coupling(name = 'GC_11',
                 value = '-6*Ca**3*complex(0,1)*lam1*Sa + 3*Ca**3*complex(0,1)*lam3*Sa + 6*Ca*complex(0,1)*lam2*Sa**3 - 3*Ca*complex(0,1)*lam3*Sa**3',
                 order = {'QED':2})

GC_12 = Coupling(name = 'GC_12',
                 value = '6*Ca**3*complex(0,1)*lam2*Sa - 3*Ca**3*complex(0,1)*lam3*Sa - 6*Ca*complex(0,1)*lam1*Sa**3 + 3*Ca*complex(0,1)*lam3*Sa**3',
                 order = {'QED':2})

GC_13 = Coupling(name = 'GC_13',
                 value = '-6*Ca**4*complex(0,1)*lam2 - 6*Ca**2*complex(0,1)*lam3*Sa**2 - 6*complex(0,1)*lam1*Sa**4',
                 order = {'QED':2})

GC_14 = Coupling(name = 'GC_14',
                 value = '-6*Ca**4*complex(0,1)*lam1 - 6*Ca**2*complex(0,1)*lam3*Sa**2 - 6*complex(0,1)*lam2*Sa**4',
                 order = {'QED':2})

GC_15 = Coupling(name = 'GC_15',
                 value = '-(Ca**4*complex(0,1)*lam3) - 6*Ca**2*complex(0,1)*lam1*Sa**2 - 6*Ca**2*complex(0,1)*lam2*Sa**2 + 4*Ca**2*complex(0,1)*lam3*Sa**2 - complex(0,1)*lam3*Sa**4',
                 order = {'QED':2})

GC_16 = Coupling(name = 'GC_16',
                 value = '(complex(0,1)*g1p*Sp)/3.',
                 order = {'QED':1})

GC_17 = Coupling(name = 'GC_17',
                 value = '-(complex(0,1)*g1p*Sp)',
                 order = {'QED':1})

GC_18 = Coupling(name = 'GC_18',
                 value = '-((ee**2*complex(0,1))/sw**2)',
                 order = {'QED':2})

GC_19 = Coupling(name = 'GC_19',
                 value = '(Ca**2*ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_20 = Coupling(name = 'GC_20',
                 value = '(Cp**2*cw**2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_21 = Coupling(name = 'GC_21',
                 value = '(Ca*ee**2*complex(0,1)*Sa)/(2.*sw**2)',
                 order = {'QED':2})

GC_22 = Coupling(name = 'GC_22',
                 value = '(ee**2*complex(0,1)*Sa**2)/(2.*sw**2)',
                 order = {'QED':2})

GC_23 = Coupling(name = 'GC_23',
                 value = '-((Cp*cw**2*ee**2*complex(0,1)*Sp)/sw**2)',
                 order = {'QED':2})

GC_24 = Coupling(name = 'GC_24',
                 value = '(cw**2*ee**2*complex(0,1)*Sp**2)/sw**2',
                 order = {'QED':2})

GC_25 = Coupling(name = 'GC_25',
                 value = '(Can1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_26 = Coupling(name = 'GC_26',
                 value = '(Can2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_27 = Coupling(name = 'GC_27',
                 value = '(Can3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_28 = Coupling(name = 'GC_28',
                 value = '(CKM1x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_29 = Coupling(name = 'GC_29',
                 value = '(CKM1x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_30 = Coupling(name = 'GC_30',
                 value = '(CKM1x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_31 = Coupling(name = 'GC_31',
                 value = '(CKM2x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_32 = Coupling(name = 'GC_32',
                 value = '(CKM2x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_33 = Coupling(name = 'GC_33',
                 value = '(CKM2x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_34 = Coupling(name = 'GC_34',
                 value = '(CKM3x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_35 = Coupling(name = 'GC_35',
                 value = '(CKM3x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_36 = Coupling(name = 'GC_36',
                 value = '(CKM3x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_37 = Coupling(name = 'GC_37',
                 value = '-(Cp*cw*ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_38 = Coupling(name = 'GC_38',
                 value = '(Cp*cw*ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_39 = Coupling(name = 'GC_39',
                 value = '(Cp*cw*ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_40 = Coupling(name = 'GC_40',
                 value = '(-2*Cp*cw*ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_41 = Coupling(name = 'GC_41',
                 value = '-((ee*complex(0,1)*San1)/(sw*cmath.sqrt(2)))',
                 order = {'QED':1})

GC_42 = Coupling(name = 'GC_42',
                 value = '-((ee*complex(0,1)*San2)/(sw*cmath.sqrt(2)))',
                 order = {'QED':1})

GC_43 = Coupling(name = 'GC_43',
                 value = '-((ee*complex(0,1)*San3)/(sw*cmath.sqrt(2)))',
                 order = {'QED':1})

GC_44 = Coupling(name = 'GC_44',
                 value = '-(cw*ee*complex(0,1)*Sp)/(2.*sw)',
                 order = {'QED':1})

GC_45 = Coupling(name = 'GC_45',
                 value = '(cw*ee*complex(0,1)*Sp)/(2.*sw)',
                 order = {'QED':1})

GC_46 = Coupling(name = 'GC_46',
                 value = '-((cw*ee*complex(0,1)*Sp)/sw)',
                 order = {'QED':1})

GC_47 = Coupling(name = 'GC_47',
                 value = '(2*cw*ee**2*complex(0,1)*Sp)/sw',
                 order = {'QED':2})

GC_48 = Coupling(name = 'GC_48',
                 value = '(complex(0,1)*gt*Sp)/6. - (Cp*ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_49 = Coupling(name = 'GC_49',
                 value = '-(complex(0,1)*gt*Sp)/2. + (Cp*ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_50 = Coupling(name = 'GC_50',
                 value = 'Can1**2*complex(0,1)*g1p*Sp + (Can1**2*complex(0,1)*gt*Sp)/2. - complex(0,1)*g1p*San1**2*Sp - (Can1**2*Cp*cw*ee*complex(0,1))/(2.*sw) - (Can1**2*Cp*ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_51 = Coupling(name = 'GC_51',
                 value = 'Can2**2*complex(0,1)*g1p*Sp + (Can2**2*complex(0,1)*gt*Sp)/2. - complex(0,1)*g1p*San2**2*Sp - (Can2**2*Cp*cw*ee*complex(0,1))/(2.*sw) - (Can2**2*Cp*ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_52 = Coupling(name = 'GC_52',
                 value = 'Can3**2*complex(0,1)*g1p*Sp + (Can3**2*complex(0,1)*gt*Sp)/2. - complex(0,1)*g1p*San3**2*Sp - (Can3**2*Cp*cw*ee*complex(0,1))/(2.*sw) - (Can3**2*Cp*ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_53 = Coupling(name = 'GC_53',
                 value = '-2*Can1*complex(0,1)*g1p*San1*Sp - (Can1*complex(0,1)*gt*San1*Sp)/2. + (Can1*Cp*cw*ee*complex(0,1)*San1)/(2.*sw) + (Can1*Cp*ee*complex(0,1)*San1*sw)/(2.*cw)',
                 order = {'QED':1})

GC_54 = Coupling(name = 'GC_54',
                 value = '-(Can1**2*complex(0,1)*g1p*Sp) + complex(0,1)*g1p*San1**2*Sp + (complex(0,1)*gt*San1**2*Sp)/2. - (Cp*cw*ee*complex(0,1)*San1**2)/(2.*sw) - (Cp*ee*complex(0,1)*San1**2*sw)/(2.*cw)',
                 order = {'QED':1})

GC_55 = Coupling(name = 'GC_55',
                 value = '-2*Can2*complex(0,1)*g1p*San2*Sp - (Can2*complex(0,1)*gt*San2*Sp)/2. + (Can2*Cp*cw*ee*complex(0,1)*San2)/(2.*sw) + (Can2*Cp*ee*complex(0,1)*San2*sw)/(2.*cw)',
                 order = {'QED':1})

GC_56 = Coupling(name = 'GC_56',
                 value = '-(Can2**2*complex(0,1)*g1p*Sp) + complex(0,1)*g1p*San2**2*Sp + (complex(0,1)*gt*San2**2*Sp)/2. - (Cp*cw*ee*complex(0,1)*San2**2)/(2.*sw) - (Cp*ee*complex(0,1)*San2**2*sw)/(2.*cw)',
                 order = {'QED':1})

GC_57 = Coupling(name = 'GC_57',
                 value = '-2*Can3*complex(0,1)*g1p*San3*Sp - (Can3*complex(0,1)*gt*San3*Sp)/2. + (Can3*Cp*cw*ee*complex(0,1)*San3)/(2.*sw) + (Can3*Cp*ee*complex(0,1)*San3*sw)/(2.*cw)',
                 order = {'QED':1})

GC_58 = Coupling(name = 'GC_58',
                 value = '-(Can3**2*complex(0,1)*g1p*Sp) + complex(0,1)*g1p*San3**2*Sp + (complex(0,1)*gt*San3**2*Sp)/2. - (Cp*cw*ee*complex(0,1)*San3**2)/(2.*sw) - (Cp*ee*complex(0,1)*San3**2*sw)/(2.*cw)',
                 order = {'QED':1})

GC_59 = Coupling(name = 'GC_59',
                 value = '(Cp*complex(0,1)*gt)/6. + (ee*complex(0,1)*Sp*sw)/(6.*cw)',
                 order = {'QED':1})

GC_60 = Coupling(name = 'GC_60',
                 value = '-(Cp*complex(0,1)*gt)/2. - (ee*complex(0,1)*Sp*sw)/(2.*cw)',
                 order = {'QED':1})

GC_61 = Coupling(name = 'GC_61',
                 value = 'Can1**2*Cp*complex(0,1)*g1p + (Can1**2*Cp*complex(0,1)*gt)/2. - Cp*complex(0,1)*g1p*San1**2 + (Can1**2*cw*ee*complex(0,1)*Sp)/(2.*sw) + (Can1**2*ee*complex(0,1)*Sp*sw)/(2.*cw)',
                 order = {'QED':1})

GC_62 = Coupling(name = 'GC_62',
                 value = 'Can2**2*Cp*complex(0,1)*g1p + (Can2**2*Cp*complex(0,1)*gt)/2. - Cp*complex(0,1)*g1p*San2**2 + (Can2**2*cw*ee*complex(0,1)*Sp)/(2.*sw) + (Can2**2*ee*complex(0,1)*Sp*sw)/(2.*cw)',
                 order = {'QED':1})

GC_63 = Coupling(name = 'GC_63',
                 value = 'Can3**2*Cp*complex(0,1)*g1p + (Can3**2*Cp*complex(0,1)*gt)/2. - Cp*complex(0,1)*g1p*San3**2 + (Can3**2*cw*ee*complex(0,1)*Sp)/(2.*sw) + (Can3**2*ee*complex(0,1)*Sp*sw)/(2.*cw)',
                 order = {'QED':1})

GC_64 = Coupling(name = 'GC_64',
                 value = '-2*Can1*Cp*complex(0,1)*g1p*San1 - (Can1*Cp*complex(0,1)*gt*San1)/2. - (Can1*cw*ee*complex(0,1)*San1*Sp)/(2.*sw) - (Can1*ee*complex(0,1)*San1*Sp*sw)/(2.*cw)',
                 order = {'QED':1})

GC_65 = Coupling(name = 'GC_65',
                 value = '-(Can1**2*Cp*complex(0,1)*g1p) + Cp*complex(0,1)*g1p*San1**2 + (Cp*complex(0,1)*gt*San1**2)/2. + (cw*ee*complex(0,1)*San1**2*Sp)/(2.*sw) + (ee*complex(0,1)*San1**2*Sp*sw)/(2.*cw)',
                 order = {'QED':1})

GC_66 = Coupling(name = 'GC_66',
                 value = '-2*Can2*Cp*complex(0,1)*g1p*San2 - (Can2*Cp*complex(0,1)*gt*San2)/2. - (Can2*cw*ee*complex(0,1)*San2*Sp)/(2.*sw) - (Can2*ee*complex(0,1)*San2*Sp*sw)/(2.*cw)',
                 order = {'QED':1})

GC_67 = Coupling(name = 'GC_67',
                 value = '-(Can2**2*Cp*complex(0,1)*g1p) + Cp*complex(0,1)*g1p*San2**2 + (Cp*complex(0,1)*gt*San2**2)/2. + (cw*ee*complex(0,1)*San2**2*Sp)/(2.*sw) + (ee*complex(0,1)*San2**2*Sp*sw)/(2.*cw)',
                 order = {'QED':1})

GC_68 = Coupling(name = 'GC_68',
                 value = '-2*Can3*Cp*complex(0,1)*g1p*San3 - (Can3*Cp*complex(0,1)*gt*San3)/2. - (Can3*cw*ee*complex(0,1)*San3*Sp)/(2.*sw) - (Can3*ee*complex(0,1)*San3*Sp*sw)/(2.*cw)',
                 order = {'QED':1})

GC_69 = Coupling(name = 'GC_69',
                 value = '-(Can3**2*Cp*complex(0,1)*g1p) + Cp*complex(0,1)*g1p*San3**2 + (Cp*complex(0,1)*gt*San3**2)/2. + (cw*ee*complex(0,1)*San3**2*Sp)/(2.*sw) + (ee*complex(0,1)*San3**2*Sp*sw)/(2.*cw)',
                 order = {'QED':1})

GC_70 = Coupling(name = 'GC_70',
                 value = 'Ca**2*Cp**2*ee**2*complex(0,1) + (Ca**2*complex(0,1)*gt**2*Sp**2)/2. + 8*complex(0,1)*g1p**2*Sa**2*Sp**2 + (Ca**2*Cp**2*cw**2*ee**2*complex(0,1))/(2.*sw**2) - (Ca**2*Cp*cw*ee*complex(0,1)*gt*Sp)/sw - (Ca**2*Cp*ee*complex(0,1)*gt*Sp*sw)/cw + (Ca**2*Cp**2*ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_71 = Coupling(name = 'GC_71',
                 value = 'Ca*Cp**2*ee**2*complex(0,1)*Sa - 8*Ca*complex(0,1)*g1p**2*Sa*Sp**2 + (Ca*complex(0,1)*gt**2*Sa*Sp**2)/2. + (Ca*Cp**2*cw**2*ee**2*complex(0,1)*Sa)/(2.*sw**2) - (Ca*Cp*cw*ee*complex(0,1)*gt*Sa*Sp)/sw - (Ca*Cp*ee*complex(0,1)*gt*Sa*Sp*sw)/cw + (Ca*Cp**2*ee**2*complex(0,1)*Sa*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_72 = Coupling(name = 'GC_72',
                 value = 'Cp**2*ee**2*complex(0,1)*Sa**2 + 8*Ca**2*complex(0,1)*g1p**2*Sp**2 + (complex(0,1)*gt**2*Sa**2*Sp**2)/2. + (Cp**2*cw**2*ee**2*complex(0,1)*Sa**2)/(2.*sw**2) - (Cp*cw*ee*complex(0,1)*gt*Sa**2*Sp)/sw - (Cp*ee*complex(0,1)*gt*Sa**2*Sp*sw)/cw + (Cp**2*ee**2*complex(0,1)*Sa**2*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_73 = Coupling(name = 'GC_73',
                 value = '-(Ca**2*Cp*ee**2*complex(0,1)*Sp) + (Ca**2*Cp*complex(0,1)*gt**2*Sp)/2. + 8*Cp*complex(0,1)*g1p**2*Sa**2*Sp - (Ca**2*Cp*cw**2*ee**2*complex(0,1)*Sp)/(2.*sw**2) - (Ca**2*Cp**2*cw*ee*complex(0,1)*gt)/(2.*sw) + (Ca**2*cw*ee*complex(0,1)*gt*Sp**2)/(2.*sw) - (Ca**2*Cp**2*ee*complex(0,1)*gt*sw)/(2.*cw) + (Ca**2*ee*complex(0,1)*gt*Sp**2*sw)/(2.*cw) - (Ca**2*Cp*ee**2*complex(0,1)*Sp*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_74 = Coupling(name = 'GC_74',
                 value = '-(Ca*Cp*ee**2*complex(0,1)*Sa*Sp) - 8*Ca*Cp*complex(0,1)*g1p**2*Sa*Sp + (Ca*Cp*complex(0,1)*gt**2*Sa*Sp)/2. - (Ca*Cp*cw**2*ee**2*complex(0,1)*Sa*Sp)/(2.*sw**2) - (Ca*Cp**2*cw*ee*complex(0,1)*gt*Sa)/(2.*sw) + (Ca*cw*ee*complex(0,1)*gt*Sa*Sp**2)/(2.*sw) - (Ca*Cp**2*ee*complex(0,1)*gt*Sa*sw)/(2.*cw) + (Ca*ee*complex(0,1)*gt*Sa*Sp**2*sw)/(2.*cw) - (Ca*Cp*ee**2*complex(0,1)*Sa*Sp*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_75 = Coupling(name = 'GC_75',
                 value = '8*Ca**2*Cp*complex(0,1)*g1p**2*Sp - Cp*ee**2*complex(0,1)*Sa**2*Sp + (Cp*complex(0,1)*gt**2*Sa**2*Sp)/2. - (Cp*cw**2*ee**2*complex(0,1)*Sa**2*Sp)/(2.*sw**2) - (Cp**2*cw*ee*complex(0,1)*gt*Sa**2)/(2.*sw) + (cw*ee*complex(0,1)*gt*Sa**2*Sp**2)/(2.*sw) - (Cp**2*ee*complex(0,1)*gt*Sa**2*sw)/(2.*cw) + (ee*complex(0,1)*gt*Sa**2*Sp**2*sw)/(2.*cw) - (Cp*ee**2*complex(0,1)*Sa**2*Sp*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_76 = Coupling(name = 'GC_76',
                 value = '(Ca**2*Cp**2*complex(0,1)*gt**2)/2. + 8*Cp**2*complex(0,1)*g1p**2*Sa**2 + Ca**2*ee**2*complex(0,1)*Sp**2 + (Ca**2*cw**2*ee**2*complex(0,1)*Sp**2)/(2.*sw**2) + (Ca**2*Cp*cw*ee*complex(0,1)*gt*Sp)/sw + (Ca**2*Cp*ee*complex(0,1)*gt*Sp*sw)/cw + (Ca**2*ee**2*complex(0,1)*Sp**2*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_77 = Coupling(name = 'GC_77',
                 value = '-8*Ca*Cp**2*complex(0,1)*g1p**2*Sa + (Ca*Cp**2*complex(0,1)*gt**2*Sa)/2. + Ca*ee**2*complex(0,1)*Sa*Sp**2 + (Ca*cw**2*ee**2*complex(0,1)*Sa*Sp**2)/(2.*sw**2) + (Ca*Cp*cw*ee*complex(0,1)*gt*Sa*Sp)/sw + (Ca*Cp*ee*complex(0,1)*gt*Sa*Sp*sw)/cw + (Ca*ee**2*complex(0,1)*Sa*Sp**2*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_78 = Coupling(name = 'GC_78',
                 value = '8*Ca**2*Cp**2*complex(0,1)*g1p**2 + (Cp**2*complex(0,1)*gt**2*Sa**2)/2. + ee**2*complex(0,1)*Sa**2*Sp**2 + (cw**2*ee**2*complex(0,1)*Sa**2*Sp**2)/(2.*sw**2) + (Cp*cw*ee*complex(0,1)*gt*Sa**2*Sp)/sw + (Cp*ee*complex(0,1)*gt*Sa**2*Sp*sw)/cw + (ee**2*complex(0,1)*Sa**2*Sp**2*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_79 = Coupling(name = 'GC_79',
                 value = '(Ca*ee**2*complex(0,1)*v)/(2.*sw**2)',
                 order = {'QED':1})

GC_80 = Coupling(name = 'GC_80',
                 value = '(ee**2*complex(0,1)*Sa*v)/(2.*sw**2)',
                 order = {'QED':1})

GC_81 = Coupling(name = 'GC_81',
                 value = '(Cp**2*complex(0,1)*gt**2*Sa*v)/2. + ee**2*complex(0,1)*Sa*Sp**2*v + (cw**2*ee**2*complex(0,1)*Sa*Sp**2*v)/(2.*sw**2) + (Cp*cw*ee*complex(0,1)*gt*Sa*Sp*v)/sw + (Cp*ee*complex(0,1)*gt*Sa*Sp*sw*v)/cw + (ee**2*complex(0,1)*Sa*Sp**2*sw**2*v)/(2.*cw**2) + 8*Ca*Cp**2*complex(0,1)*g1p**2*x',
                 order = {'QED':1})

GC_82 = Coupling(name = 'GC_82',
                 value = '(Ca*Cp**2*complex(0,1)*gt**2*v)/2. + Ca*ee**2*complex(0,1)*Sp**2*v + (Ca*cw**2*ee**2*complex(0,1)*Sp**2*v)/(2.*sw**2) + (Ca*Cp*cw*ee*complex(0,1)*gt*Sp*v)/sw + (Ca*Cp*ee*complex(0,1)*gt*Sp*sw*v)/cw + (Ca*ee**2*complex(0,1)*Sp**2*sw**2*v)/(2.*cw**2) - 8*Cp**2*complex(0,1)*g1p**2*Sa*x',
                 order = {'QED':1})

GC_83 = Coupling(name = 'GC_83',
                 value = '-6*Ca**2*complex(0,1)*lam1*Sa*v + 2*Ca**2*complex(0,1)*lam3*Sa*v - complex(0,1)*lam3*Sa**3*v - Ca**3*complex(0,1)*lam3*x - 6*Ca*complex(0,1)*lam2*Sa**2*x + 2*Ca*complex(0,1)*lam3*Sa**2*x',
                 order = {'QED':1})

GC_84 = Coupling(name = 'GC_84',
                 value = '-3*Ca**2*complex(0,1)*lam3*Sa*v - 6*complex(0,1)*lam1*Sa**3*v - 6*Ca**3*complex(0,1)*lam2*x - 3*Ca*complex(0,1)*lam3*Sa**2*x',
                 order = {'QED':1})

GC_85 = Coupling(name = 'GC_85',
                 value = '-6*Ca**3*complex(0,1)*lam1*v - 3*Ca*complex(0,1)*lam3*Sa**2*v + 3*Ca**2*complex(0,1)*lam3*Sa*x + 6*complex(0,1)*lam2*Sa**3*x',
                 order = {'QED':1})

GC_86 = Coupling(name = 'GC_86',
                 value = '-(Ca**3*complex(0,1)*lam3*v) - 6*Ca*complex(0,1)*lam1*Sa**2*v + 2*Ca*complex(0,1)*lam3*Sa**2*v + 6*Ca**2*complex(0,1)*lam2*Sa*x - 2*Ca**2*complex(0,1)*lam3*Sa*x + complex(0,1)*lam3*Sa**3*x',
                 order = {'QED':1})

GC_87 = Coupling(name = 'GC_87',
                 value = '-(Cp*ee**2*complex(0,1)*Sa*Sp*v) + (Cp*complex(0,1)*gt**2*Sa*Sp*v)/2. - (Cp*cw**2*ee**2*complex(0,1)*Sa*Sp*v)/(2.*sw**2) - (Cp**2*cw*ee*complex(0,1)*gt*Sa*v)/(2.*sw) + (cw*ee*complex(0,1)*gt*Sa*Sp**2*v)/(2.*sw) - (Cp**2*ee*complex(0,1)*gt*Sa*sw*v)/(2.*cw) + (ee*complex(0,1)*gt*Sa*Sp**2*sw*v)/(2.*cw) - (Cp*ee**2*complex(0,1)*Sa*Sp*sw**2*v)/(2.*cw**2) + 8*Ca*Cp*complex(0,1)*g1p**2*Sp*x',
                 order = {'QED':1})

GC_88 = Coupling(name = 'GC_88',
                 value = '-(Ca*Cp*ee**2*complex(0,1)*Sp*v) + (Ca*Cp*complex(0,1)*gt**2*Sp*v)/2. - (Ca*Cp*cw**2*ee**2*complex(0,1)*Sp*v)/(2.*sw**2) - (Ca*Cp**2*cw*ee*complex(0,1)*gt*v)/(2.*sw) + (Ca*cw*ee*complex(0,1)*gt*Sp**2*v)/(2.*sw) - (Ca*Cp**2*ee*complex(0,1)*gt*sw*v)/(2.*cw) + (Ca*ee*complex(0,1)*gt*Sp**2*sw*v)/(2.*cw) - (Ca*Cp*ee**2*complex(0,1)*Sp*sw**2*v)/(2.*cw**2) - 8*Cp*complex(0,1)*g1p**2*Sa*Sp*x',
                 order = {'QED':1})

GC_89 = Coupling(name = 'GC_89',
                 value = 'Cp**2*ee**2*complex(0,1)*Sa*v + (complex(0,1)*gt**2*Sa*Sp**2*v)/2. + (Cp**2*cw**2*ee**2*complex(0,1)*Sa*v)/(2.*sw**2) - (Cp*cw*ee*complex(0,1)*gt*Sa*Sp*v)/sw - (Cp*ee*complex(0,1)*gt*Sa*Sp*sw*v)/cw + (Cp**2*ee**2*complex(0,1)*Sa*sw**2*v)/(2.*cw**2) + 8*Ca*complex(0,1)*g1p**2*Sp**2*x',
                 order = {'QED':1})

GC_90 = Coupling(name = 'GC_90',
                 value = 'Ca*Cp**2*ee**2*complex(0,1)*v + (Ca*complex(0,1)*gt**2*Sp**2*v)/2. + (Ca*Cp**2*cw**2*ee**2*complex(0,1)*v)/(2.*sw**2) - (Ca*Cp*cw*ee*complex(0,1)*gt*Sp*v)/sw - (Ca*Cp*ee*complex(0,1)*gt*Sp*sw*v)/cw + (Ca*Cp**2*ee**2*complex(0,1)*sw**2*v)/(2.*cw**2) - 8*complex(0,1)*g1p**2*Sa*Sp**2*x',
                 order = {'QED':1})

GC_91 = Coupling(name = 'GC_91',
                 value = '-((Ca*complex(0,1)*yb)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_92 = Coupling(name = 'GC_92',
                 value = '-((complex(0,1)*Sa*yb)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_93 = Coupling(name = 'GC_93',
                 value = '-((Ca*complex(0,1)*yc)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_94 = Coupling(name = 'GC_94',
                 value = '-((complex(0,1)*Sa*yc)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_95 = Coupling(name = 'GC_95',
                 value = '-((Ca*complex(0,1)*ydo)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_96 = Coupling(name = 'GC_96',
                 value = '-((complex(0,1)*Sa*ydo)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_97 = Coupling(name = 'GC_97',
                 value = '-((Ca*complex(0,1)*ye)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_98 = Coupling(name = 'GC_98',
                 value = '-((complex(0,1)*Sa*ye)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_99 = Coupling(name = 'GC_99',
                 value = '-((Ca*complex(0,1)*ym)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_100 = Coupling(name = 'GC_100',
                  value = '-((complex(0,1)*Sa*ym)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_101 = Coupling(name = 'GC_101',
                  value = 'Can1*complex(0,1)*Sa*San1*ynd1*cmath.sqrt(2) - Ca*Can1**2*complex(0,1)*ynm1*cmath.sqrt(2)',
                  order = {'QED':1})

GC_102 = Coupling(name = 'GC_102',
                  value = 'Ca*Can1*complex(0,1)*San1*ynd1*cmath.sqrt(2) + Can1**2*complex(0,1)*Sa*ynm1*cmath.sqrt(2)',
                  order = {'QED':1})

GC_103 = Coupling(name = 'GC_103',
                  value = '-((Can1**2*complex(0,1)*Sa*ynd1)/cmath.sqrt(2)) + (complex(0,1)*Sa*San1**2*ynd1)/cmath.sqrt(2) - Ca*Can1*complex(0,1)*San1*ynm1*cmath.sqrt(2)',
                  order = {'QED':1})

GC_104 = Coupling(name = 'GC_104',
                  value = '-((Ca*Can1**2*complex(0,1)*ynd1)/cmath.sqrt(2)) + (Ca*complex(0,1)*San1**2*ynd1)/cmath.sqrt(2) + Can1*complex(0,1)*Sa*San1*ynm1*cmath.sqrt(2)',
                  order = {'QED':1})

GC_105 = Coupling(name = 'GC_105',
                  value = 'Can1*complex(0,1)*Sa*San1*ynd1*cmath.sqrt(2) + Ca*complex(0,1)*San1**2*ynm1*cmath.sqrt(2)',
                  order = {'QED':1})

GC_106 = Coupling(name = 'GC_106',
                  value = 'Ca*Can1*complex(0,1)*San1*ynd1*cmath.sqrt(2) - complex(0,1)*Sa*San1**2*ynm1*cmath.sqrt(2)',
                  order = {'QED':1})

GC_107 = Coupling(name = 'GC_107',
                  value = 'Can2*complex(0,1)*Sa*San2*ynd2*cmath.sqrt(2) - Ca*Can2**2*complex(0,1)*ynm2*cmath.sqrt(2)',
                  order = {'QED':1})

GC_108 = Coupling(name = 'GC_108',
                  value = 'Ca*Can2*complex(0,1)*San2*ynd2*cmath.sqrt(2) + Can2**2*complex(0,1)*Sa*ynm2*cmath.sqrt(2)',
                  order = {'QED':1})

GC_109 = Coupling(name = 'GC_109',
                  value = '-((Can2**2*complex(0,1)*Sa*ynd2)/cmath.sqrt(2)) + (complex(0,1)*Sa*San2**2*ynd2)/cmath.sqrt(2) - Ca*Can2*complex(0,1)*San2*ynm2*cmath.sqrt(2)',
                  order = {'QED':1})

GC_110 = Coupling(name = 'GC_110',
                  value = '-((Ca*Can2**2*complex(0,1)*ynd2)/cmath.sqrt(2)) + (Ca*complex(0,1)*San2**2*ynd2)/cmath.sqrt(2) + Can2*complex(0,1)*Sa*San2*ynm2*cmath.sqrt(2)',
                  order = {'QED':1})

GC_111 = Coupling(name = 'GC_111',
                  value = 'Can2*complex(0,1)*Sa*San2*ynd2*cmath.sqrt(2) + Ca*complex(0,1)*San2**2*ynm2*cmath.sqrt(2)',
                  order = {'QED':1})

GC_112 = Coupling(name = 'GC_112',
                  value = 'Ca*Can2*complex(0,1)*San2*ynd2*cmath.sqrt(2) - complex(0,1)*Sa*San2**2*ynm2*cmath.sqrt(2)',
                  order = {'QED':1})

GC_113 = Coupling(name = 'GC_113',
                  value = 'Can3*complex(0,1)*Sa*San3*ynd3*cmath.sqrt(2) - Ca*Can3**2*complex(0,1)*ynm3*cmath.sqrt(2)',
                  order = {'QED':1})

GC_114 = Coupling(name = 'GC_114',
                  value = 'Ca*Can3*complex(0,1)*San3*ynd3*cmath.sqrt(2) + Can3**2*complex(0,1)*Sa*ynm3*cmath.sqrt(2)',
                  order = {'QED':1})

GC_115 = Coupling(name = 'GC_115',
                  value = '-((Can3**2*complex(0,1)*Sa*ynd3)/cmath.sqrt(2)) + (complex(0,1)*Sa*San3**2*ynd3)/cmath.sqrt(2) - Ca*Can3*complex(0,1)*San3*ynm3*cmath.sqrt(2)',
                  order = {'QED':1})

GC_116 = Coupling(name = 'GC_116',
                  value = '-((Ca*Can3**2*complex(0,1)*ynd3)/cmath.sqrt(2)) + (Ca*complex(0,1)*San3**2*ynd3)/cmath.sqrt(2) + Can3*complex(0,1)*Sa*San3*ynm3*cmath.sqrt(2)',
                  order = {'QED':1})

GC_117 = Coupling(name = 'GC_117',
                  value = 'Can3*complex(0,1)*Sa*San3*ynd3*cmath.sqrt(2) + Ca*complex(0,1)*San3**2*ynm3*cmath.sqrt(2)',
                  order = {'QED':1})

GC_118 = Coupling(name = 'GC_118',
                  value = 'Ca*Can3*complex(0,1)*San3*ynd3*cmath.sqrt(2) - complex(0,1)*Sa*San3**2*ynm3*cmath.sqrt(2)',
                  order = {'QED':1})

GC_119 = Coupling(name = 'GC_119',
                  value = '-((Ca*complex(0,1)*ys)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_120 = Coupling(name = 'GC_120',
                  value = '-((complex(0,1)*Sa*ys)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_121 = Coupling(name = 'GC_121',
                  value = '-((Ca*complex(0,1)*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_122 = Coupling(name = 'GC_122',
                  value = '-((complex(0,1)*Sa*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_123 = Coupling(name = 'GC_123',
                  value = '-((Ca*complex(0,1)*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_124 = Coupling(name = 'GC_124',
                  value = '-((complex(0,1)*Sa*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_125 = Coupling(name = 'GC_125',
                  value = '-((Ca*complex(0,1)*yup)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_126 = Coupling(name = 'GC_126',
                  value = '-((complex(0,1)*Sa*yup)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_127 = Coupling(name = 'GC_127',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_128 = Coupling(name = 'GC_128',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_129 = Coupling(name = 'GC_129',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x3))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_130 = Coupling(name = 'GC_130',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_131 = Coupling(name = 'GC_131',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_132 = Coupling(name = 'GC_132',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x3))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_133 = Coupling(name = 'GC_133',
                  value = '(ee*complex(0,1)*complexconjugate(CKM3x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_134 = Coupling(name = 'GC_134',
                  value = '(ee*complex(0,1)*complexconjugate(CKM3x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_135 = Coupling(name = 'GC_135',
                  value = '(ee*complex(0,1)*complexconjugate(CKM3x3))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

# KH


GC_KH_Gup = Coupling(name = 'GC_KH_Gup',
                  value = 'gqq*complex(0,1)',
                  order = {'QED':1})


GC_KH_Gdown = Coupling(name = 'GC_KH_Gdown',
                  value = 'GC_KH_Gup*xi',
                  order = {'QED':1})

GC_KH_Gchi = Coupling(name = 'GC_KH_Gchi',
                  value = 'gDM*complex(0,1)',
                  order = {'QED':1})
