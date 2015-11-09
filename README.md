# cebolato~~r~~l

Translator tool from any langue to Cebolinha's dialect.

## What is it?

It is a simple tool to turn any text to a kind of dialect. Actually it is not a dialect, it is just a funny way of speaking by a very popular character of brazilian culture. The character's name is [Cebolinha](https://en.wikipedia.org/wiki/Jimmy_Five) and he appears on the comic books of [Turma da Monica](https://en.wikipedia.org/wiki/Monica%27s_Gang), created by cartoonist [Mauricio de Sousa](https://en.wikipedia.org/wiki/Mauricio_de_Sousa).

## Why?

No idea.

## What can I do with it?

We don't know, have some fun?

## How do I use it?

cebolatol provides two different ways to interact with it, an RESTful API that can be accessed as specified below and an small web application available [here](http://cebolatol.julianofernandes.com.br). In either cases you sends your message and receives the same one translated.

### API

How explained before it is a very simple application and its API provides one single resource to query `/api/tlanslate`. One single parameter is required `message` containing, obviously, the message to be translated. The project is hosted [here](http://cebolatol.julianofernandes.com.br) and the example will reference to that address.

* Request details
	* **RESOURCE** /api/tlanslate
	* **METHOD** POST
	* **PARAM** _String_ message

#### Example

Performing the request using the command line tool _curl_.

	$ curl -X POST http://cebolatol.julianofernandes.com.br/api/tlanslate \
		-H 'Content-Type: application/json' \
		-d '{"message": "my text to be translated"}'

Then the response will be a json object containing the message translated.

	{
		"phlase": "my text to be tlanslated"
	}

If the required parameter was not sent the response should be as follow.

	{
		"ellol": "You must pass a message"
	}

## Finally

If you have some doubt, let us know. If you found some use for this, let us know too.

That's all folks. **Enjoy!**

```
                                                :-                                                
                                               -y                                                 
                    -:://++++oo+/:.'          'd-         '-/+++///::::-'                         
                               '.:osys/.      +h      .+yyo/-'                                    
                                     ./shy/'  yo   :sho:'                                         
                                         .ohh/h+'+ho.                                             
                              ''.--:/++ooosshNNdmmsooooo+++///::---.'''                           
                   ''-:/+osyyyyso++/---......'.'''''...----:::/+++ossyyyhhso+/-.'                 
            '.:+shdyso+:-.''                                            .odo-:/+oooo+/-'          
       ./ossso//hh-          -++++/.                     -///oo+.         'oh:      '.://++/-'    
  ./ooo/-'    /d/          /y/'   ':+.                 -/.     -ss.         'yy.            .::'  
-/:.        'sy.         'y+         .                .-         :d.          /d+:/:.             
        :ossyd-         'y/                                       :d'        'sh+--/oh+'          
      -hs.   'o/        os                                         so       'h/      'yd.         
     /m:       .       'd-                                         .d'      :/        'hh         
    -m:                -h          ''                   ''          h.                 .M:        
   'hs                 :y        /mMMm/               /dMMd:        y-                  mo        
   -m-                 -y       +MMMMMM/             oMMMMMN:       y.                  mo        
   /m.                 'y'     .mMMMMMMd'           -NMMMMMMs       y'                 'N/        
   /m.                  +:     -NMMNNMMN.           /MMNmNMMh      -o                  /N.        
   .m/                  .s'    .mN/''-mN.           :Ns' 'oMs      o'                 'dy         
    yh'       :/         -+     sm-  'dh'    ''     'ds' 'om.     /-        '+'       om'         
    .mo      /s           -:    '+mmdNh.  '++//+o:   .hNmmy.     ..          /d'     +N-          
     -m+    -d.                   '.-.    o/    'h'    '.'                    hy   'om-           
      .dy.  oh'                           .+.   +/                            oN. :hy.            
       '+ds-sd'                                                               oNshy-              
          :odN-                  .-                       +-                 'my-'                
            'hh'                 '/o+-                ./o+.                 'hm.                  
             'hh.                   ':dhs+/:---::/oydNMh'                  .hm.                   
              'sm/                    .mMMMMMmddhdmNMMd'                  /my'                    
                -dh:                   -mNy:.'     '+h.                 :hd:                      
                  /dh/'                 -y-        /o'               '/dh:                        
                    -ymy:'               'oo-   '/s:              ':yms-                          
                      '/ymy/.              ':+++/.            ':ohmy:'                            
                         '-ohhs/-'                       '-/shdy+-                                
                             '-+shhyo+:--..''''''.-:/+shddyo:.                                    
                                  ''-:/+osssyyyyyyso+/-.'                                         
```