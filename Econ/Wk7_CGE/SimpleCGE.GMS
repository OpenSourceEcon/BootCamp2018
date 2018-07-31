*$ A simple CGE model for KSA, code follows Hosoe et al (2004)


* Definition of sets for suffix ---------------------------------------
Set     u       SAM entry                /AGR, OIL, IND, SER, LAB, CAP, LAND, NTR, DTX, IDT, ACT, HOH, GOV,
                                          INV, EXT/
        i(u)    goods                    /AGR, OIL, IND, SER/
        h(u)    factor                   /LAB, CAP, LAND, NTR/
        w(h)    non-capital factor       /LAB, LAND, NTR/

Alias (u,v), (i,j), (h,k);
* ---------------------------------------------------------------------

* Loading data --------------------------------------------------------
Table   SAM(u,v)        social accounting matrix
           AGR      OIL      IND       SER       LAB      CAP      LAND     NTR
AGR        7        2        56        15        0        0        0        0
OIL        0        4        134       11        0        0        0        0
IND        15       13       316       312       0        0        0        0
SER        9        8        147       250       0        0        0        0
LAB        7        28       87        429       0        0        0        0
CAP        26       68       351       606       0        0        0        0
LAND       24       0        0         0         0        0        0        0
NTR        0        890.435  0         0         0        0        0        0
DTX        0        0        0         0         0        0        0        0
IDT        1        0        20        0         0        0        0        0
ACT        -4       0        1         12        0        0        0        0
HOH        0        0        0         0         551      1051     24       890.435
GOV        0        0        0         0         0        0        0        0
INV        0        0        0         0         0        0        0        0
EXT        33       2        626       202       0        0        0        0



+        DTX        IDT      ACT      HOH      GOV      INV      EXT
AGR        0        0        0        34       2        0        2
OIL        0        0        0        0        0        0        866.435
IND        0        0        0        396      265      115      306
SER        0        0        0        408      611      370      34
LAB        0        0        0        0        0        0        0
CAP        0        0        0        0        0        0        0
LAND       0        0        0        0        0        0        0
NTR        0        0        0        0        0        0        0
DTX        0        0        0        948      0        0        0
IDT        0        0        0        0        0        0        0
ACT        0        0        0        0        0        0        0
HOH        0        0        0        0        100      0        0
GOV        948      21       9        0        0        0        0
INV        0        0        0        189      0        0        296
EXT        0        0        0        641.435  0        0        0

;


* Loading the initial values ------------------------------------------
Parameter       Y0(j)           composite factor
                F0(h,j)         the h-th factor input by the j-th firm
                X0(i,j)         intermediate input
                XX0(j)          total intermediate inputs by the j-th sector
                Z0(j)           output of the j-th good
                Xp0(i)          household consumption of the i-th good
                Xg0(i)          government consumption
                Xv0(i)          investment demand
                E0(i)           exports
                M0(i)           imports
                Q0(i)           Armington's composite good
                D0(i)           domestic good
                Sp0             private saving
                Sg0             government saving
                Td0             direct tax
                Trf0            transfers from gov to household
                Tz0(j)          production tax
                Tm0(j)          import tariff

                FF0(h)          factor endowment of the h-th factor
                Sf0             foreign saving in US dollars
                pWe(i)          export price in US dollars
                pWm(i)          import price in US dollars
                tauz(i)         production tax rate
                taum(i)         import tariff rate

                YY0             aggregate factor income
                XXp0            aggregate consumption
                XXv0            aggregate investment
                XXg0            aggregate government consumption
                MM0             aggregate imports
                EE0             aggregate exports
                GDP0            Gross Domestic Product

                FSH0            repatriation of profits
                KK0             capital stock
                KD0             domestically-owned capital stock
                KF0             foreign-owned capital stock
                g               long-run growth rate
                R0              Rate of return on domestic investment
;

KK0 = 10510;
KF0 = 6414.35;
KD0 = KK0 - KF0;



Td0     =SAM("DTX","HOH");
Trf0    =SAM("HOH","GOV");
Tz0(j)  =SAM("ACT",j);
Tm0(j)  =SAM("IDT",J);

FSH0    =SAM("EXT","HOH");

F0(h,j) =SAM(h,j);
Y0(j)   =sum(h, F0(h,j));
YY0     =sum(j, Y0(j));
X0(i,j) =SAM(i,j);
XX0(i)  =sum(j, X0(j,i));
Z0(j)   =Y0(j) +sum(i, X0(i,j));
M0(i)   =SAM("EXT",i);
MM0     =sum(i,M0(i));

tauz(j) =Tz0(j)/Z0(j);
taum(j) =Tm0(j)/M0(j);

Xp0(i)  =SAM(i,"HOH");
XXp0    =sum(i,Xp0(i));
FF0(h)  =SAM("HOH",h);

R0 = FF0("CAP")/KK0;

Xg0(i)  =SAM(i,"GOV");
XXg0    =sum(i,Xg0(i));
Xv0(i)  =SAM(i,"INV");
XXv0    =sum(i,Xv0(i));
E0(i)   =SAM(i,"EXT");
EE0     =sum(i,E0(i));
Q0(i)   =Xp0(i)+Xg0(i)+Xv0(i)+sum(j, X0(i,j));
D0(i)   =(1+tauz(i))*Z0(i)-E0(i);
Sp0     =SAM("INV","HOH");
Sg0     =SAM("INV","GOV");

pWe(i)  =1;
pWm(i)  =1;

Sf0     =sum(i, pWm(i)*M0(i))+FSH0 - sum(i, pWe(i)*E0(i));

GDP0 = XXp0 + XXg0 + XXv0 + EE0 - MM0;

g = XXv0/KK0;



Display Y0,F0,X0,Z0,Xp0,Xg0,Xv0,E0,M0,Q0,D0,Sp0,Sg0,Td0,Tz0,Tm0,Trf0,
        FF0,Sf0,tauz,taum, FSH0,GDP0,XX0;

* Calibration ---------------------------------------------------------
Parameter       sigma(i)        elasticity of substitution
                psi(i)          elasticity of transformation
                eta(i)          substitution elasticity parameter
                phi(i)          transformation elasticity parameter
;

sigma(i)=3;
psi(i)  =3;

sigma("OIL")=1.2;
psi("OIL")  =1.2;

eta(i)=(sigma(i)-1)/sigma(i);
phi(i)=(psi(i)+1)/psi(i);

Parameter       alpha(i)        share parameter in utility func.
                beta(h,j)       share parameter in production func.
                b(j)            scale parameter in production func.
                ax(i,j)         intermediate input requirement coeff.
                ay(j)           composite fact. input req. coeff.
                mu(i)           government consumption share
                lambda(i)       investment demand share
                deltam(i)       share par. in Armington func.
                deltad(i)       share par. in Armington func.
                gamma(i)        scale par. in Armington func.
                xid(i)          share par. in transformation func.
                xie(i)          share par. in transformation func.
                theta(i)        scale par. in transformation func.
                ssp             average propensity for private saving
                taud            direct tax rate
                tautr           transfer rate from gov to h'hold
                ginc
                hinc


;

alpha(i)=Xp0(i)/sum(j, Xp0(j));
beta(h,j)=F0(h,j)/sum(k, F0(k,j));
b(j)    =Y0(j)/prod(h, F0(h,j)**beta(h,j));

ax(i,j) =X0(i,j)/Z0(j);
ay(j)   =Y0(j)/Z0(j);
mu(i)   =Xg0(i)/sum(j, Xg0(j));
lambda(i)=Xv0(i)/(Sp0+Sg0+Sf0);

deltam(i)=(1+taum(i))*M0(i)**(1-eta(i))
          /((1+taum(i))*M0(i)**(1-eta(i)) +D0(i)**(1-eta(i)));
deltad(i)=D0(i)**(1-eta(i))
          /((1+taum(i))*M0(i)**(1-eta(i)) +D0(i)**(1-eta(i)));
gamma(i)=Q0(i)/(deltam(i)*M0(i)**eta(i)+deltad(i)*D0(i)**eta(i))
         **(1/eta(i));

xie(i)=E0(i)**(1-phi(i))/(E0(i)**(1-phi(i))+D0(i)**(1-phi(i)));
xid(i)=D0(i)**(1-phi(i))/(E0(i)**(1-phi(i))+D0(i)**(1-phi(i)));
theta(i)=Z0(i)
         /(xie(i)*E0(i)**phi(i)+xid(i)*D0(i)**phi(i))**(1/phi(i));

ssp     =Sp0/(sum(h, FF0(h)) - FSH0 + Trf0);
taud    =Td0/sum(h, FF0(h));
tautr   =Trf0/FF0("LAB");
ginc    =Td0+sum(j, Tz0(j))+sum(j, Tm0(j));
hinc    =sum(h, FF0(h));


Display alpha,beta,b,ax,ay,mu,lambda,deltam,deltad,gamma,xie,
        xid,theta,ssp,taud,tautr,ginc,hinc;
* ---------------------------------------------------------------------

* Defining model system -----------------------------------------------
Variable        Y(j)            composite factor
                F(h,j)          the h-th factor input by the j-th firm
                X(i,j)          intermediate input
                Z(j)            output of the j-th good
                Xp(i)           household consumption of the i-th good
                Xg(i)           government consumption
                Xv(i)           investment demand
                E(i)            exports
                M(i)            imports
                Q(i)            Armington's composite good
                D(i)            domestic good

                pf(h)           the h-th factor price
                py(j)           composite factor price
                pz(j)           supply price of the i-th good
                pq(i)           Armington's composite good price
                pe(i)           export price in local currency
                pm(i)           import price in local currency
                pd(i)           the i-th domestic good price
                epsilon         exchange rate

                Sp              private saving
                Sf              foreign saving
                Sg              government saving
                Td              direct tax
                Trf             transfers from gov to h'hold
                Tz(j)           production tax
                Tm(i)           import tariff

                YY              aggregate factor income
                XXp             aggregate consumption
                XXv             aggregate investment
                XXg             aggregate government consumption
                MM              aggregate imports
                EE              aggregate exports
                GDP             Gross Domestic Product

                FSH             repatriation of profits
                KK              capital stock
                KD              domestically-owned capital stock
                KF              foreign-owned capital stock
                R               Rate of return on domestic investment

                FF(h)           factor endowment of the h-th factor

                UU              utility [fictitious]
;

Equation        eqpy(j)         composite factor agg. func.
                eqF(h,j)        factor demand function
                eqX(i,j)        intermediate demand function
                eqY(j)          composite factor demand function
                eqpzs(j)        unit cost function

                eqTd            direct tax revenue function
                eqTrf           transfers to h'hold from gov function
                eqTz(j)         production tax revenue function
                eqTm(i)         import tariff revenue function
                eqXg(i)         government demand function

                eqXv(i)         investment demand function
                eqSp            private saving function
                eqSg            government saving function
                eqSf            market clearing for investment

                eqXp(i)         household demand function

                eqpe(i)         world export price equation
                eqpm(i)         world import price equation
                eqepsilon       balance of payments

                eqpqs(i)        Armington function
                eqM(i)          import demand function
                eqD(i)          domestic good demand function

                eqpzd(i)        transformation function
                eqDs(i)         domestic good supply function
                eqE(i)          export supply function

                eqpqd(i)        market clearing cond. for comp. good
                eqpf(w)         factor market clearing condition
                eqpk           factor market clearing condition

                eqYY            aggregate factor income
                eqXXp           aggregate consumption
                eqXXv           aggregate investment
                eqMM            aggregate imports
                eqEE            aggregate exports
                eqGDP           Gross Domestic Product

                eqFSH           repatriation of profits
                eqKD            domestically owned capital
                eqKF            foreign owned capital
                eqKK            capital stock

*                obj             utility function [fictitious]
;
*[domestic production] ----
eqpy(j)..       Y(j)    =e= b(j)*prod(h, F(h,j)**beta(h,j));
eqF(h,j)..      F(h,j)  =e= beta(h,j)*py(j)*Y(j)/pf(h);
eqX(i,j)..      X(i,j)  =e= ax(i,j)*Z(j);
eqY(j)..        Y(j)    =e= ay(j)*Z(j);
eqpzs(j)..      pz(j)   =e= ay(j)*py(j) +sum(i, ax(i,j)*pq(i));

*[government behavior] ----
eqTd..          Td      =e= taud*sum(h, pf(h)*FF(h));
eqTrf..         Trf     =e= tautr*pf("LAB")*FF("LAB");
eqTz(j)..       Tz(j)   =e= tauz(j)*pz(j)*Z(j);
eqTm(i)..       Tm(i)   =e= taum(i)*pm(i)*M(i);
eqXg(i)..       Xg(i)   =e= mu(i)* XXg;


*[investment behavior] ----
eqXv(i)..       Xv(i)   =e= lambda(i)*(XXv);

*[savings] ----------------
eqSp..          Sp      =e= ssp*(sum(h, pf(h)*FF(h)) - FSH + Trf);
eqSg..          Sg      =e= (Td +sum(j, Tz(j))+sum(j, Tm(j))) - (Trf + XXg*sum(i,mu(i)*pq(i)));

eqFSH..         FSH     =e= R*Kf*epsilon;

eqKD..          Sp      =e= g*KD*sum(i, lambda(i)*pq(i));
eqKF..          KF      =e= KK - KD;
eqKK..          R       =e= ((pf("Cap")*FF("Cap")/KK)/sum(i, lambda(i)*pq(i)));


*[household consumption] --
eqXp(i)..       Xp(i)   =e= alpha(i)*(sum(h, pf(h)*FF(h)) -Sp -Td -FSH +Trf)
                            /pq(i);

*[international trade] ----
eqpe(i)..       pe(i)   =e= epsilon*pWe(i);
eqpm(i)..       pm(i)   =e= epsilon*pWm(i);
eqepsilon..          sum(i, pWe(i)*E(i)) +Sf/epsilon
                        =e= sum(i, pWm(i)*M(i)) + FSH/epsilon;
eqSf..          Sf     =e= g*Kf*sum(i, lambda(i)*pq(i)) ;

*[Armington function] -----
eqpqs(i)..      Q(i)    =e= gamma(i)*(deltam(i)*M(i)**eta(i)+deltad(i)
                            *D(i)**eta(i))**(1/eta(i));
eqM(i)..        M(i)    =e= (gamma(i)**eta(i)*deltam(i)*pq(i)
                            /((1+taum(i))*pm(i)))**(1/(1-eta(i)))*Q(i);
eqD(i)..        D(i)    =e= (gamma(i)**eta(i)*deltad(i)*pq(i)/pd(i))
                            **(1/(1-eta(i)))*Q(i);

*[transformation function] -----
eqpzd(i)..      Z(i)    =e= theta(i)*(xie(i)*E(i)**phi(i)+xid(i)
                            *D(i)**phi(i))**(1/phi(i));
eqE(i)..        E(i)    =e= (theta(i)**phi(i)*xie(i)*(1+tauz(i))*pz(i)
                            /pe(i))**(1/(1-phi(i)))*Z(i);
eqDs(i)..       D(i)    =e= (theta(i)**phi(i)*xid(i)*(1+tauz(i))*pz(i)
                            /pd(i))**(1/(1-phi(i)))*Z(i);

*[market clearing condition]
eqpqd(i)..      Q(i)    =e= Xp(i) +Xg(i) +Xv(i) +sum(j, X(i,j));
eqpf(w)..       sum(j, F(w,j)) =e= FF(w);
eqpk..          sum(j,F("CAP",j)) =e= KK/KK0*FF0("CAP");

*[aggregates]
eqYY..          YY      =e=sum(i,Y(i));
eqXXp..         XXp     =e=sum(i,Xp(i));
eqXXv..         XXv     =e= g*KK;

eqMM..          MM      =e=sum(i,M(i));
eqEE..          EE      =e=sum(i,E(i));
eqGDP..         GDP     =e= XXp + XXv + XXg + EE - MM;

*[fictitious objective function]
*obj..           UU      =e= prod(i, Xp(i)**alpha(i));
* ---------------------------------------------------------------------

* Initializing variables ----------------------------------------------
Y.l(j)  =Y0(j);
F.l(h,j)=F0(h,j);
X.l(i,j)=X0(i,j);
Z.l(j)  =Z0(j);
Xp.l(i) =Xp0(i);
Xg.l(i) =Xg0(i);
Xv.l(i) =Xv0(i);
E.l(i)  =E0(i);
M.l(i)  =M0(i);
Q.l(i)  =Q0(i);
D.l(i)  =D0(i);
pf.l(h) =1;
py.l(j) =1;
pz.l(j) =1;
pq.l(i) =1;
pe.l(i) =1;
pm.l(i) =1;
pd.l(i) =1;
epsilon.l=1;
Sp.l    =Sp0;
Td.l    =Td0;
Trf.l   =Trf0;
Tz.l(j) =Tz0(j);
Tm.l(i) =Tm0(i);
YY.l    =YY0;
XXp.l   =XXp0;
XXv.l   =XXv0;

MM.l    =MM0;
EE.l    =EE0;

FSH.l    =FSH0;
KK.l     =KK0;
KD.l     =KD0;
KF.l     =KF0;

FF.fx(h)    =FF0(h);
FF.l("CAP") =FF0("CAP");
FF.lo("CAP") =-inf;
FF.up("CAP") =+inf;

*Closures
*Fixed budget balance, government consumption adjusts to hit target balance
Sg.fx   =Sg0;
XXg.l   =XXg0;
XXg.lo  =-inf;
XXg.up  =+inf;


*Capital Account
$ontext
*Perfectly elastic supply of foreign funds
R.fx = R0;
Sf.l = Sf0;
Sf.lo  =-inf;
Sf.up  =+inf;
$offtext


*$ontext
*Fixed supply of foreign funds
R.l = R0;
R.lo  =-inf;
R.up  =+inf;
Sf.fx = Sf0;
*$offtext

* numeraire ---
epsilon.fx=1;

* ---------------------------------------------------------------------
* Defining and solving the model --------------------------------------
Model stdcge /all/;


*Solve stdcge maximizing UU using nlp;
Solve stdcge using mcp;

parameter check;
check = (Sf.l + Sg.l + Sp.l)/sum(i, lambda(i)*pq.l(i)) - XXv.l;

Display check;
*$stop

* ---------------------------------------------------------------------
* Simulation Runs
*Increase production tax on industry by 5%
*tauz("ind") = tauz("ind")+0.05;

*b("AGR")=b("AGR")*1.1;

pWe("OIL") = 1.1;

*R.fx = R0*1.03

*neutrality
*epsilon.fx = 1*1.03;
*Sf.fx = Sf0*1.03;

*constant returns to scale
*FF.fx(w)= FF.l(w)*1.1;
*Sf.fx = Sf0*1.1;


Solve stdcge using mcp;
*Solve stdcge maximizing UU using nlp;

check = (Sf.l + Sg.l + Sp.l)/sum(i, lambda(i)*pq.l(i)) - XXv.l;
Display check;

* ---------------------------------------------------------------------
* ---------------------------------------------------------------------
* List8.1: Display of changes ------------------------------------------
Parameter
dY(j),dF(h,j),dX(i,j),dZ(j),dXp(i),dXg(i),dXv(i),
dE(i),dM(i),dQ(i),dD(i),dpf(h),dpy(j),dpz(i),dpq(i),
dpe(i),dpm(i),dpd(i),depsilon,dTd,dTrf,dTz(i),dTm(i),dSp,dSg,dSf,
dYY,dXXp,dXXg,dXXv,dMM,dEE, dFSH, dGDP, dR, dKK, dKD, dKF, dFF(h);
;

dY(j)$(Y0(j) ne 0)    =(Y.l(j)  /Y0(j)  -1)*100;
dF(h,j)$(F0(h,j) ne 0)=(F.l(h,j)/F0(h,j)-1)*100;
dFF(h)$(FF0(h) ne 0)  =(FF.l(h)/FF0(h)-1)*100;
dX(i,j)$(X0(i,j) ne 0)=(X.l(i,j)/X0(i,j)-1)*100;
dZ(j)$(Z0(j) ne 0)    =(Z.l(j)  /Z0(j)  -1)*100;
dXp(i)$(Xp0(i) ne 0)  =(Xp.l(i) /Xp0(i) -1)*100;
dXg(i)$(Xg0(i) ne 0)  =(Xg.l(i) /Xg0(i) -1)*100;
dXv(i)$(Xv0(i) ne 0)  =(Xv.l(i) /Xv0(i) -1)*100;
dE(i)$(E0(i) ne 0)    =(E.l(i)  /E0(i)  -1)*100;
dM(i)$(M0(i) ne 0)    =(M.l(i)  /M0(i)  -1)*100;
dQ(i)$(Q0(i) ne 0)    =(Q.l(i)  /Q0(i)  -1)*100;
dD(i)$(D0(i) ne 0)    =(D.l(i)  /D0(i)  -1)*100;
dpf(h)                =(pf.l(h) /1 -1)*100;
dpy(j)                =(py.l(j) /1 -1)*100;
dpz(j)                =(pz.l(j) /1 -1)*100;
dpq(i)                =(pq.l(i) /1 -1)*100;
dpe(i)                =(pe.l(i) /1 -1)*100;
dpm(i)                =(pm.l(i) /1 -1)*100;
dpd(i)                =(pd.l(i) /1 -1)*100;
depsilon              =(epsilon.l/1 -1)*100;
dTd$(Td0 ne 0)        =(Td.l    /Td0    -1)*100;
dTrf$(Trf0 ne 0)      =(Trf.l   /Trf0   -1)*100;
*dTrfROW$(TrfROW0 ne 0)=(TrfROW.l   /TrfROW0   -1)*100;
dTz(j)$(Tz0(j) ne 0)  =(Tz.l(j) /Tz0(j) -1)*100;
dTm(i)$(Tm0(i) ne 0)  =(Tm.l(i) /Tm0(i) -1)*100;
dSp$(Sp0 ne 0)        =(Sp.l    /Sp0    -1)*100;
dSg$(Sg0 ne 0)        =(Sg.l    /Sg0    -1)*100;
dSf$(Sf0 ne 0)        =(Sf.l    /Sf0    -1)*100;
dYY$(YY0 ne 0)        =(YY.l    /YY0    -1)*100;
dXXp$(XXp0 ne 0)      =(XXp.l   /XXp0   -1)*100;
dXXg$(XXg0 ne 0)      =(XXg.l   /XXg0   -1)*100;
dXXv$(XXv0 ne 0)      =(XXv.l   /XXv0   -1)*100;
dMM$(MM0 ne 0)        =(MM.l    /MM0    -1)*100;
dEE$(EE0 ne 0)        =(EE.l    /EE0    -1)*100;
dGDP$(GDP0 ne 0)      =(GDP.l    /GDP0  -1)*100;

*dFSG$(FSG0 ne 0)      =(FSG.l    /FSG0    -1)*100;
dFSH$(FSH0 ne 0)      =(FSH.l    /FSH0    -1)*100;
dR                    =(R.l    -R0    )*100;
dKK                    =(KK.l    /KK0    -1)*100;
dKD                    =(KD.l    /KD0    -1)*100;
dKF                    =(KF.l    /KF0    -1)*100;

Display
dY,dF,dX,dZ,dXp,dXg,dXv,dE,dM,dQ,dD,dpf,dpy,dpz,
dpq,dpe,dpm,dpd,depsilon,dTd,dTrf,dTz,dTm,dSp,dSg,dSf,dFSH,
dYY,dXXp,dXXg,dXXv,dMM,dEE,XXp.l,XXg.l,XXv.l,EE.l,MM.l,b, dGDP, GDP.l, dR, dKK, dKD, dKF, dFF;

$stop

* Welfare measure: Hicksian equivalent variations ---------------------
Parameter       UU0             utility level in the Base Run Eq.
                ep0             expenditure func. in the Base Run Eq.
                ep1             expenditure func. in the C-f Eq.
                EV              Hicksian equivalent variations
;
UU0     =prod(i, Xp0(i)**alpha(i));
ep0     =UU0 /prod(i, (alpha(i)/1)**alpha(i));
ep1     =UU.l/prod(i, (alpha(i)/1)**alpha(i));
EV      =ep1-ep0;

Display EV;

* ---------------------------------------------------------------------
* List A.1: an example of CSV file generation
File listA1out /listA1.csv/;
Put listA1out;
listA1out.pc=5;

* putting a note
Put "This is an example of usage of the Put command." / /;

* putting dXp(i)
Put "dXp(i)" /;
Loop(i,
     Put i.tl, dXp(i) /;
     );
Put / /;

* putting Imports
Put "Imports" /;
Loop(i,
     Put i.tl, dM(i) /;
     );
Put / /;

* putting dTd
Put "dTd" dTd /;
Put / /;

* putting F(h,j)
Put "F(h,j)" /;
Put ""; Loop(j, Put j.tl); Put /;
Loop(h, Put h.tl; Loop(j, Put F.l(h,j);); Put /;);
Put / /;

* putting beta(h,j)
Put "beta(h,j)" /;
Put ""; Loop(j, Put j.tl); Put /;
Loop(h, Put h.tl; Loop(j, Put beta(h,j);); Put /;);
Put / /;

* putting dGDP
Put "dGDP" dGDP /;
Put / / ;

* putting value added
Put "Value added" /;
Loop(i,
     Put i.tl, y.l(i) /;
     );
Put / /;



* end of CSV output
* ---------------------------------------------------------------------
* end of model --------------------------------------------------------
* ---------------------------------------------------------------------

