# This file was automatically created by FeynRules 2.0.28
# Mathematica version: 9.0 for Linux x86 (64-bit) (February 7, 2013)
# Date: Tue 7 Oct 2014 18:10:49


from __future__ import division
from object_library import all_particles, Particle
import parameters as Param

import propagators as Prop

n1 = Particle(pdg_code = 12,
              name = 'n1',
              antiname = 'n1',
              spin = 2,
              color = 1,
              mass = Param.MnL1,
              width = Param.ZERO,
              texname = 'n1',
              antitexname = 'n1',
              charge = 0,
              BarionLepton = 0,
              GhostNumber = 0,
              LeptonNumber = 0)

n2 = Particle(pdg_code = 14,
              name = 'n2',
              antiname = 'n2',
              spin = 2,
              color = 1,
              mass = Param.MnL2,
              width = Param.ZERO,
              texname = 'n2',
              antitexname = 'n2',
              charge = 0,
              BarionLepton = 0,
              GhostNumber = 0,
              LeptonNumber = 0)

n3 = Particle(pdg_code = 16,
              name = 'n3',
              antiname = 'n3',
              spin = 2,
              color = 1,
              mass = Param.MnL3,
              width = Param.ZERO,
              texname = 'n3',
              antitexname = 'n3',
              charge = 0,
              BarionLepton = 0,
              GhostNumber = 0,
              LeptonNumber = 0)

P__tilde__n1 = Particle(pdg_code = 9100012,
                        name = '~n1',
                        antiname = 'Xn1',
                        spin = 2,
                        color = 1,
                        mass = Param.MnH1,
                        width = Param.WnH1,
                        texname = '~n1',
                        antitexname = 'Xn1',
                        charge = 0,
                        BarionLepton = 0,
                        GhostNumber = 0,
                        LeptonNumber = 0)

P__n1 = P__tilde__n1.anti()

P__tilde__n2 = Particle(pdg_code = 9100014,
                        name = '~n2',
                        antiname = 'Xn2',
                        spin = 2,
                        color = 1,
                        mass = Param.MnH2,
                        width = Param.WnH2,
                        texname = '~n2',
                        antitexname = 'Xn2',
                        charge = 0,
                        BarionLepton = 0,
                        GhostNumber = 0,
                        LeptonNumber = 0)

P__n2 = P__tilde__n2.anti()

P__tilde__n3 = Particle(pdg_code = 9100016,
                        name = '~n3',
                        antiname = 'Xn3',
                        spin = 2,
                        color = 1,
                        mass = Param.MnH3,
                        width = Param.WnH3,
                        texname = '~n3',
                        antitexname = 'Xn3',
                        charge = 0,
                        BarionLepton = 0,
                        GhostNumber = 0,
                        LeptonNumber = 0)

P__n3 = P__tilde__n3.anti()


e = Particle(pdg_code = 11,
             name = 'e',
             antiname = 'E',
             spin = 2,
             color = 1,
             mass = Param.ME,
             width = Param.ZERO,
             texname = 'e',
             antitexname = 'E',
             charge = -1,
             BarionLepton = -1,
             GhostNumber = 0,
             LeptonNumber = 1)

E = e.anti()

m = Particle(pdg_code = 13,
             name = 'm',
             antiname = 'M',
             spin = 2,
             color = 1,
             mass = Param.MM,
             width = Param.ZERO,
             texname = 'm',
             antitexname = 'M',
             charge = -1,
             BarionLepton = -1,
             GhostNumber = 0,
             LeptonNumber = 1)

M = m.anti()

l = Particle(pdg_code = 15,
             name = 'l',
             antiname = 'L',
             spin = 2,
             color = 1,
             mass = Param.MTA,
             width = Param.ZERO,
             texname = 'l',
             antitexname = 'L',
             charge = -1,
             BarionLepton = -1,
             GhostNumber = 0,
             LeptonNumber = 1)

L = l.anti()

u = Particle(pdg_code = 2,
             name = 'u',
             antiname = 'U',
             spin = 2,
             color = 3,
             mass = Param.MU,
             width = Param.ZERO,
             texname = 'u',
             antitexname = 'U',
             charge = 2/3,
             BarionLepton = 1/3,
             GhostNumber = 0,
             LeptonNumber = 0)

U = u.anti()

c = Particle(pdg_code = 4,
             name = 'c',
             antiname = 'C',
             spin = 2,
             color = 3,
             mass = Param.MC,
             width = Param.ZERO,
             texname = 'c',
             antitexname = 'C',
             charge = 2/3,
             BarionLepton = 1/3,
             GhostNumber = 0,
             LeptonNumber = 0)

C = c.anti()

t = Particle(pdg_code = 6,
             name = 't',
             antiname = 'T',
             spin = 2,
             color = 3,
             mass = Param.MT,
             width = Param.WT,
             texname = 't',
             antitexname = 'T',
             charge = 2/3,
             BarionLepton = 1/3,
             GhostNumber = 0,
             LeptonNumber = 0)

T = t.anti()

d = Particle(pdg_code = 1,
             name = 'd',
             antiname = 'D',
             spin = 2,
             color = 3,
             mass = Param.MD,
             width = Param.ZERO,
             texname = 'd',
             antitexname = 'D',
             charge = -1/3,
             BarionLepton = 1/3,
             GhostNumber = 0,
             LeptonNumber = 0)

D = d.anti()

s = Particle(pdg_code = 3,
             name = 's',
             antiname = 'S',
             spin = 2,
             color = 3,
             mass = Param.MS,
             width = Param.ZERO,
             texname = 's',
             antitexname = 'S',
             charge = -1/3,
             BarionLepton = 1/3,
             GhostNumber = 0,
             LeptonNumber = 0)

S = s.anti()

b = Particle(pdg_code = 5,
             name = 'b',
             antiname = 'B',
             spin = 2,
             color = 3,
             mass = Param.MB,
             width = Param.ZERO,
             texname = 'b',
             antitexname = 'B',
             charge = -1/3,
             BarionLepton = 1/3,
             GhostNumber = 0,
             LeptonNumber = 0)

B = b.anti()

ghA = Particle(pdg_code = 9000001,
               name = 'ghA',
               antiname = 'ghA~',
               spin = -1,
               color = 1,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'ghA',
               antitexname = 'ghA~',
               charge = 0,
               BarionLepton = 0,
               GhostNumber = 1,
               LeptonNumber = 0)

ghA__tilde__ = ghA.anti()

ghZ = Particle(pdg_code = 9000002,
               name = 'ghZ',
               antiname = 'ghZ~',
               spin = -1,
               color = 1,
               mass = Param.MZ,
               width = Param.ZERO,
               texname = 'ghZ',
               antitexname = 'ghZ~',
               charge = 0,
               BarionLepton = 0,
               GhostNumber = 1,
               LeptonNumber = 0)

ghZ__tilde__ = ghZ.anti()

ghWp = Particle(pdg_code = 9000003,
                name = 'ghWp',
                antiname = 'ghWp~',
                spin = -1,
                color = 1,
                mass = Param.MW,
                width = Param.ZERO,
                texname = 'ghWp',
                antitexname = 'ghWp~',
                charge = 1,
                BarionLepton = 0,
                GhostNumber = 1,
                LeptonNumber = 0)

ghWp__tilde__ = ghWp.anti()

ghWm = Particle(pdg_code = 9000004,
                name = 'ghWm',
                antiname = 'ghWm~',
                spin = -1,
                color = 1,
                mass = Param.MW,
                width = Param.ZERO,
                texname = 'ghWm',
                antitexname = 'ghWm~',
                charge = -1,
                BarionLepton = 0,
                GhostNumber = 1,
                LeptonNumber = 0)

ghWm__tilde__ = ghWm.anti()

ghG = Particle(pdg_code = 9000005,
               name = 'ghG',
               antiname = 'ghG~',
               spin = -1,
               color = 8,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'ghG',
               antitexname = 'ghG~',
               charge = 0,
               BarionLepton = 0,
               GhostNumber = 1,
               LeptonNumber = 0)

ghG__tilde__ = ghG.anti()

ghZp = Particle(pdg_code = 9000006,
                name = 'ghZp',
                antiname = 'ghZp~',
                spin = -1,
                color = 1,
                mass = Param.MZp,
                width = Param.ZERO,
                texname = 'ghZp',
                antitexname = 'ghZp~',
                charge = 0,
                BarionLepton = 0,
                GhostNumber = 1,
                LeptonNumber = 0)

ghZp__tilde__ = ghZp.anti()

A = Particle(pdg_code = 22,
             name = 'A',
             antiname = 'A',
             spin = 3,
             color = 1,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'A',
             antitexname = 'A',
             charge = 0,
             BarionLepton = 0,
             GhostNumber = 0,
             LeptonNumber = 0)

Z = Particle(pdg_code = 23,
             name = 'Z',
             antiname = 'Z',
             spin = 3,
             color = 1,
             mass = Param.MZ,
             width = Param.WZ,
             texname = 'Z',
             antitexname = 'Z',
             charge = 0,
             BarionLepton = 0,
             GhostNumber = 0,
             LeptonNumber = 0)

W__plus__ = Particle(pdg_code = 24,
                     name = 'W+',
                     antiname = 'W-',
                     spin = 3,
                     color = 1,
                     mass = Param.MW,
                     width = Param.WW,
                     texname = 'W+',
                     antitexname = 'W-',
                     charge = 1,
                     BarionLepton = 0,
                     GhostNumber = 0,
                     LeptonNumber = 0)

W__minus__ = W__plus__.anti()

G = Particle(pdg_code = 21,
             name = 'G',
             antiname = 'G',
             spin = 3,
             color = 8,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'G',
             antitexname = 'G',
             charge = 0,
             BarionLepton = 0,
             GhostNumber = 0,
             LeptonNumber = 0)

Zp = Particle(pdg_code = 9900032,
              name = 'Zp',
              antiname = 'Zp',
              spin = 3,
              color = 1,
              mass = Param.MZp,
              width = Param.WZp,
              texname = 'Zp',
              antitexname = 'Zp',
              charge = 0,
              BarionLepton = 0,
              GhostNumber = 0,
              LeptonNumber = 0)

H1 = Particle(pdg_code = 9900025,
              name = 'H1',
              antiname = 'H1',
              spin = 1,
              color = 1,
              mass = Param.MH1,
              width = Param.WH1,
              texname = 'H1',
              antitexname = 'H1',
              charge = 0,
              BarionLepton = 0,
              GhostNumber = 0,
              LeptonNumber = 0)

phiZ = Particle(pdg_code = 9900250,
                name = 'phiZ',
                antiname = 'phiZ',
                spin = 1,
                color = 1,
                mass = Param.MZ,
                width = Param.ZERO,
                texname = 'phiZ',
                antitexname = 'phiZ',
                goldstone = True,
                charge = 0,
                BarionLepton = 0,
                GhostNumber = 0,
                LeptonNumber = 0)

phi__plus__ = Particle(pdg_code = 9900251,
                       name = 'phi+',
                       antiname = 'phi-',
                       spin = 1,
                       color = 1,
                       mass = Param.MW,
                       width = Param.ZERO,
                       texname = 'phi+',
                       antitexname = 'phi-',
                       goldstone = True,
                       charge = 1,
                       BarionLepton = 0,
                       GhostNumber = 0,
                       LeptonNumber = 0)

phi__minus__ = phi__plus__.anti()

H2 = Particle(pdg_code = 9900026,
              name = 'H2',
              antiname = 'H2',
              spin = 1,
              color = 1,
              mass = Param.MH2,
              width = Param.WH2,
              texname = 'H2',
              antitexname = 'H2',
              charge = 0,
              BarionLepton = 0,
              GhostNumber = 0,
              LeptonNumber = 0)

phiZp = Particle(pdg_code = 9900252,
                 name = 'phiZp',
                 antiname = 'phiZp',
                 spin = 1,
                 color = 1,
                 mass = Param.MZp,
                 width = Param.ZERO,
                 texname = 'phiZp',
                 antitexname = 'phiZp',
                 goldstone = True,
                 charge = 0,
                 BarionLepton = 0,
                 GhostNumber = 0,
                 LeptonNumber = 0)

