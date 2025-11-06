from dataclasses import dataclass

from ndsl import Local, QuantityFactory, NDSLRuntime
from ndsl.constants import X_DIM, Y_DIM, Z_DIM, Z_INTERFACE_DIM


@dataclass
class Temporaries:
    t1: Local
    dp1: Local
    omq: Local
    qv0: Local
    ql0: Local
    qr0: Local
    qi0: Local
    qs0: Local
    qg0: Local
    qa0: Local
    qv1: Local
    ql1: Local
    qr1: Local
    qi1: Local
    qs1: Local
    qg1: Local
    qa1: Local
    dz1: Local
    den: Local
    den1: Local
    denfac: Local
    p_dry: Local
    m1: Local
    u1: Local
    v1: Local
    w1: Local
    onemsig: Local
    ccn: Local
    c_praut: Local
    rh_limited: Local
    ze: Local
    zt: Local
    lhi: Local
    icpk: Local
    hold_data: Local
    vti: Local
    vts: Local
    vtg: Local
    vtr: Local
    m1_sol: Local
    m1_rain: Local
    rain1: Local
    graupel1: Local
    snow1: Local
    ice1: Local
    evap1: Local
    subl1: Local

    @classmethod
    def make(cls, runtime: NDSLRuntime, quantity_factory: QuantityFactory):
        t1 = runtime.make_local(quantity_factory, [X_DIM, Y_DIM, Z_DIM])
        dp1 = runtime.make_local(quantity_factory, [X_DIM, Y_DIM, Z_DIM])
        omq = runtime.make_local(quantity_factory, [X_DIM, Y_DIM, Z_DIM])
        qv0 = runtime.make_local(quantity_factory, [X_DIM, Y_DIM, Z_DIM])
        ql0 = runtime.make_local(quantity_factory, [X_DIM, Y_DIM, Z_DIM])
        qr0 = runtime.make_local(quantity_factory, [X_DIM, Y_DIM, Z_DIM])
        qi0 = runtime.make_local(quantity_factory, [X_DIM, Y_DIM, Z_DIM])
        qs0 = runtime.make_local(quantity_factory, [X_DIM, Y_DIM, Z_DIM])
        qg0 = runtime.make_local(quantity_factory, [X_DIM, Y_DIM, Z_DIM])
        qa0 = runtime.make_local(quantity_factory, [X_DIM, Y_DIM, Z_DIM])
        qv1 = runtime.make_local(quantity_factory, [X_DIM, Y_DIM, Z_DIM])
        ql1 = runtime.make_local(quantity_factory, [X_DIM, Y_DIM, Z_DIM])
        qr1 = runtime.make_local(quantity_factory, [X_DIM, Y_DIM, Z_DIM])
        qi1 = runtime.make_local(quantity_factory, [X_DIM, Y_DIM, Z_DIM])
        qs1 = runtime.make_local(quantity_factory, [X_DIM, Y_DIM, Z_DIM])
        qg1 = runtime.make_local(quantity_factory, [X_DIM, Y_DIM, Z_DIM])
        qa1 = runtime.make_local(quantity_factory, [X_DIM, Y_DIM, Z_DIM])
        dz1 = runtime.make_local(quantity_factory, [X_DIM, Y_DIM, Z_DIM])
        den = runtime.make_local(quantity_factory, [X_DIM, Y_DIM, Z_DIM])
        den1 = runtime.make_local(quantity_factory, [X_DIM, Y_DIM, Z_DIM])
        denfac = runtime.make_local(quantity_factory, [X_DIM, Y_DIM, Z_DIM])
        p_dry = runtime.make_local(quantity_factory, [X_DIM, Y_DIM, Z_DIM])
        m1 = runtime.make_local(quantity_factory, [X_DIM, Y_DIM, Z_DIM])
        u1 = runtime.make_local(quantity_factory, [X_DIM, Y_DIM, Z_DIM])
        v1 = runtime.make_local(quantity_factory, [X_DIM, Y_DIM, Z_DIM])
        w1 = runtime.make_local(quantity_factory, [X_DIM, Y_DIM, Z_DIM])
        onemsig = runtime.make_local(quantity_factory, [X_DIM, Y_DIM])
        ccn = runtime.make_local(quantity_factory, [X_DIM, Y_DIM, Z_DIM])
        c_praut = runtime.make_local(quantity_factory, [X_DIM, Y_DIM, Z_DIM])
        rh_limited = runtime.make_local(quantity_factory, [X_DIM, Y_DIM, Z_DIM])
        ze = runtime.make_local(quantity_factory, [X_DIM, Y_DIM, Z_INTERFACE_DIM])
        zt = runtime.make_local(quantity_factory, [X_DIM, Y_DIM, Z_INTERFACE_DIM])
        lhi = runtime.make_local(quantity_factory, [X_DIM, Y_DIM, Z_DIM])
        icpk = runtime.make_local(quantity_factory, [X_DIM, Y_DIM, Z_DIM])
        hold_data = runtime.make_local(quantity_factory, [X_DIM, Y_DIM, Z_DIM])
        vti = runtime.make_local(quantity_factory, [X_DIM, Y_DIM, Z_DIM])
        vts = runtime.make_local(quantity_factory, [X_DIM, Y_DIM, Z_DIM])
        vtg = runtime.make_local(quantity_factory, [X_DIM, Y_DIM, Z_DIM])
        vtr = runtime.make_local(quantity_factory, [X_DIM, Y_DIM, Z_DIM])
        m1_sol = runtime.make_local(quantity_factory, [X_DIM, Y_DIM, Z_DIM])
        m1_rain = runtime.make_local(quantity_factory, [X_DIM, Y_DIM, Z_DIM])
        rain1 = runtime.make_local(quantity_factory, [X_DIM, Y_DIM])
        graupel1 = runtime.make_local(quantity_factory, [X_DIM, Y_DIM])
        snow1 = runtime.make_local(quantity_factory, [X_DIM, Y_DIM])
        ice1 = runtime.make_local(quantity_factory, [X_DIM, Y_DIM])
        evap1 = runtime.make_local(quantity_factory, [X_DIM, Y_DIM, Z_DIM])
        subl1 = runtime.make_local(quantity_factory, [X_DIM, Y_DIM, Z_DIM])

        return cls(
            t1,
            dp1,
            omq,
            qv0,
            ql0,
            qr0,
            qi0,
            qs0,
            qg0,
            qa0,
            qv1,
            ql1,
            qr1,
            qi1,
            qs1,
            qg1,
            qa1,
            dz1,
            den,
            den1,
            denfac,
            p_dry,
            m1,
            u1,
            v1,
            w1,
            onemsig,
            ccn,
            c_praut,
            rh_limited,
            ze,
            zt,
            lhi,
            icpk,
            hold_data,
            vti,
            vts,
            vtg,
            vtr,
            m1_sol,
            m1_rain,
            rain1,
            graupel1,
            snow1,
            ice1,
            evap1,
            subl1,
        )
