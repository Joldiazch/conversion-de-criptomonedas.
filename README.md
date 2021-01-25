### CASO SERVICIOS FINANCIEROS

Proceso de seleccion Servicios Financieros Confama

## Diagrama de la Arquitectura Actual


![](https://i.ibb.co/RcJ1Jv0/Diagrama-Arquitectura-Actual-Business-architecture-example.png)

## Propuesta de Arquitectura


![](https://i.ibb.co/4ThRxXb/Diagrama-Arquitectura-Actual-Page-2.png)

** ¿ Que componentes adicionales surgen en la arquitectura para lograr la entrega y el despliegue automáticos (DEVSECOPS) los desplegaría on-premise o en la nube ?, ¿porque? si es nube, en ¿cual nube?. Dependiendo del despliegue seleccionado especifique en donde se encuentra el código y que hacen los componentes para hacer posible el devsecops. **

La arquitectura propuesta es una arquitectura de micro servicios donde cada uno de estos servicios es independiente del otro es decir, si por alguna razon el servicio encargado de la viculacioón de nuevos clientes falla, los demás micro servicios como el de administracion de cartera seguirá funcionando sin ningun inconveniente.

La implementacion de cada uno de estos micro servicios permite aplicar DevSecOps desde su concepcion hasta su despliegue en produccion. 

Personalmente preferíria un despliegue en la nube de AWS pues esto permine escalar horizontalmente con mayor facilidad cualquiera de los microservicios en caso de ser necesario.




**¿Cuales criterios de evaluación tendría ud en cuenta para seleccionar la fabrica de
desarrollo partner de la implementación ?**

Una fabrica de desarrollo que ya haya trabajado con la compañia y cuyos resultados hayan sido satisfactorios, además que tenga experiencia en el desarrollo de servicios financieros y/o desarrollando servicios poara alguna FinTech latinoamericana.

** Desarrollar un servicio en el backend de conversión de criptomonedas **

El codigo fuente de este servicio se encuentra [aquí](https://github.com/Joldiazch/conversion-de-criptomonedas.), o bien acontinuacion hay un vistazo del codigo:
 
 ```python
import json
import requests

def converter(currency_input, amount, currency_output):
    """ Converter currencies from 
    currency in allowed_currency list to 
    another currency in this lis """

    allowed_currencies = ['BTC', 'BCC', 'LTC', 'ETH', 'ETC', 'XRP']
    data = requests.get('https://api.binance.com/api/v3/ticker/price?').json()

    # check if input data is allowed
    if currency_input in allowed_currencies and currency_output in allowed_currencies:
        if not (type(amount) is int or type(amount) is float):
            return "El monto a convertir debe ser un numero Real pero se recibio: {}".format(amount)

        symbol = currency_input + currency_output

        filter_obj = list(filter(lambda obj: obj['symbol'] == symbol, data))
        if filter_obj:
            price = filter_obj[0].get('price')
            resp = {
                'currencyInput': currency_input,
                'currencyOutput': currency_output,
                'amount': amount,
                'result': amount*float(price)
            }
            return json.dumps(resp)
        else:
            return "No se encontró factor de conversion de {} a {}".format(currency_input, currency_output)
    else:
        return "Las divisas permitidas son solo: {}".format(', '.join(allowed_currencies))


if __name__ == "__main__":
    print(converter("BCC", 100, "BTC"))
 ```



###End