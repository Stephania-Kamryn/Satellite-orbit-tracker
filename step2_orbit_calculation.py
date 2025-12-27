from sgp4.api import Satrec,jday
from datetime import datetime,timezone

line1="1 25544U 98067A   20344.91667824  .00016717  00000-0  10270-3 0  9003"
line2="2 25544  51.6442  21.4546 0002187 130.5363 329.6784 15.49315339257145"
satellite=Satrec.twoline2rv(line1,line2)
#current utc time


def get_position_velocity():
    now=datetime.now(timezone.utc)
    jd,fr=jday(now.year,now.month,now.day,now.hour,now.minute,now.second)
    e, r, v = satellite.sgp4(jd,fr)
    if e!=0:
        raise RuntimeError("Generation of position and velocity failed with error code in sgp4 as: {}".format(e))
    return r, v
position, velocity = get_position_velocity()
print("Position (km):", position)
print("Velocity (km/s):", velocity)





                      