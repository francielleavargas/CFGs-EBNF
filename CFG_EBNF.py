# -*- coding: utf-8 -*-

#Language
{mostre-me|ShowingOrViewingMarkingWord} a previsão do tempo
qual a previsão do tempo para {sexta-feira|Date}
{me mostra|ShowingOrViewingMarkingWord} a previsão do tempo para {hoje|Date} em {santa catarina|State}
qual é a previsão do tempo de {hoje|Date}
qual será o clima em {agosto|Date}
{me mostre|ShowingOrViewingMarkingWord} a previsão do tempo para {essa semana|Date}
como está a previsão do tempo {estendida|TypeOfForecast} para o {ceará|State}
qual é a previsão do tempo para {quarta-feira|Date} em {são paulo|City}
como está o clima em {altos|City} {piauí|State} {hoje|Date}
{choverá|WeatherDetail} em {berlim|City} {esta semana|Date}
vai {chover|WeatherDetail} no {final de semana|Date}
qual é a previsão para {este fim de semana|Date}
como está o tempo
qual é a previsão para às {cinco horas|Time}

#Lexicon
<showing> 	:= mostre-me | (me) (mostra | mestre)
<date> 		:= (sexta|quarta)-feira | hoje | agosto | (essa|esta) (final de|fim de) semana 
<state> 	:= santa catarina | ceará 
<city>		:= são paulo | berlim
<time> 		:= cinco horas
<typeof>	:= estendida
<wheather>	:= choverá | chover

#Rules
<forecast> := a previsão (do | para) (tempo)?

<show_the_weather> 		:= <showing> <forecast> ((para) (<date> | <data><state>))?
<how_are_the_weather>	:= (como|qual) ((está|é|será) (o tempo|o clima em) ((<date>|(<city><state><date>))))? <forecast> (<typeof>)? (para (o)?|de|às) (<time>|<date>|<state>)(<city>))			
<weather_detail> 		:= (vai)? <weather> (em | no ) (<city>? <date>)


#Final rule
<weather_forecast> := <show_the_weather> | <how_are_the_weather> | <weather_detail>
 