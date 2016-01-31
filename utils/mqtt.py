import paho.mqtt.publish as pub

def publish(msgs,broker="localhost"):
    data = []
    prefix = "/weather/"
    for k in msgs.keys():
        try:
            for k2 in msgs[k]:
                t = prefix + str(k) + '/' + str(k2)
                p = str(msgs[k][k2])
                data.append( (t,p,0,True) )
        except Exception:
            pass
        t = prefix + str(k)
        p = str(msgs[k]['value']) + " " + str(msgs[k]['unit'])
        data.append( (t,p,0,True) )
        
    pub.multiple(data, broker, port=1883, client_id="Weather")
