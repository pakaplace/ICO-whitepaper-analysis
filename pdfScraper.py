from urllib import urlopen, urlretrieve
from bs4 import BeautifulSoup
from time import sleep
import requests

# url = 'http://www.facecoin.tech'
ext = 'pdf'
urlarray = ["http://facecoin.tech/", "http://ico.nexus.social/", "http://icos.icobox.io/", "http://ico.bitdice.me/zh/", "http://aventus.io/", "http://easymine.io/", "http://ahoolee.io/", "http://stuffgogo.com/", "http://prospectors.io/en", "http://rivetzintl.com/", "http://onegram.org/", "http://filecoin.io/", "http://fujinto.io/", "http://www.alpencoin.com/", "http://www.hubii.network/", "http://revain.org/", "http://substratum.net", "http://wwam.io/", "http://coss.io/", "http://indorse.io/", "http://www.viberate.io/", "http://finshi.capital/", "http://moeda.in/", "http://atbcoin.com/", "http://xplay.fund", "http://dmarket.io/", "http://www.corion.io/", "http://www.dimcoin.io/", "http://opus-foundation.org/", "http://ico.paquarium.com/#executiveteam", "http://www.agrello.org/", "http://tokensale.tierion.com/", "http://www.blocktix.io/", "http://www.monsterbyte.io/ico", "http://santiment.net/", "http://district0x.io/", "http://suncontract.org/", "http://www.fundyourselfnow.com/#", "http://cryptonomos.com/wtt/", "http://blocktix.io/", "http://www.rootproject.co/", "http://ico.trueflip.io/", "http://www.geofounders.com/ico/", "http://primalbase.com/", "http://www.dentcoin.com/", "http://eros.vision/", "http://skincoin.org/", "http://ico.gilgam.es/ico", "http://ico.gilgam.es/", "http://pillarproject.io/", "http://coindash.io/", "http://sumerchain.com/", "http://mothership.cx/", "http://www.bitquence.com/", "http://ico.info/projects/1", "http://sonm.io/", "http://orocrypt.com/#", "http://www.fucktoken.io/", "http://www.tezos.com/", "http://insurex.co/", "http://nimiq.com/", "http://atbcoin.com/", "http://leviarcoin.org/", "http://investments.onplace.io/", "http://polybius.io/", "http://santiment.net", "http://www.openanx.org/en/", "http://www.rialto.ai/", "http://startaico.com/", "http://ico.crypviser.net/", "http://www.rialto.ai/", "http://encryptotel.com/", "http://www.adex.network/", "http://blockpool.io", "http://www.dcorp.it/crowdsale", "http://tokeninvestor.com/crowdfunding/air", "http://www.21million.co.uk/", "http://silvercoin.io/", "http://crowdsale.idice.io/", "http://octanox.org/", "http://wagerr.com/", "http://cryptoping.tech/", "http://nvo.io/", "http://www.tenx.tech/", "http://masknetwork.com/", "http://omg.omise.co/", "http://www.xfccoin.io/", "http://www.civic.com/", "http://status.im/", "http://coinstorm.net/en", "http://mona.co/", "http://www.bidlend.io/", "http://minexcoin.com/", "http://www.superdao.io/", "http://www.bancor.network/", "http://aira.life/", "http://zrcoin.io/", "http://www.ecobit.io/en/index.html", "http://cofound.it/en/", "http://voise.it/", "http://patientory.com/", "http://embermine.com/", "http://www.adelphoi.io/", "http://basicattentiontoken.org/", "http://exscudo.com/", "http://mysterium.network/", "http://www.ico.suretly.com/", "http://veritas.veritaseum.com/", "http://www.metalpay.com/", "http://mobilego.io/", "http://storj.io/index.html", "http://www.e4row.co.il/", "http://vivaco.in/", "http://aragon.one/", "http://bitcoingrowthfund.com/mcap", "http://www.peerplays.com/", "http://www.ethbits.com/", "http://legendsroomlv.com/", "http://boscoin.io/en/home/", "http://www.nexxuscoin.com/sections/company/21/nexxuscoin/index.html", "http://theqrl.org/", "http://tokencard.io/", "http://www.creativechain.org", "http://www.apptrade.io/", "http://lunyr.com/", "http://backto.earth/", "http://taas.fund/", "http://humaniq.co/", "http://gnosis.pm/", "http://iex.ec/", "http://www.wetrust.io/", "http://blockchain.capital/", "http://www.aeternity.com/", "http://cosmos.network/", "http://cosmos.network/", "http://matchpool.co/", "http://equibitgroup.com/", "http://chainofpoints.com/", "http://www.cashscripter.com/", "http://qtum.org/en/", "http://edgeless.io/", "http://www.lykke.com/", "http://www.augmentorsgame.com/", "http://www.lykke.com/", "http://contingency.tech/", "http://etheroll.com/", "http://melonport.com/", "http://chronobank.io/", "http://dfinity.network/", "http://cannabisrevolution.us/", "http://www.wings.ai/#!/home/discover", "http://betking.io/", "http://darcr.us/", "http://www.blockcdn.org/", "http://www.ether.camp/", "http://www.ether.camp/", "http://mysterium.network/", "http://www.vdice.io/", "http://ark.io/", "http://golos.io/", "http://www.incentloyalty.com/", "http://www.beyond-the-void.net/", "http://mass.network/", "http://arcade.city/", "http://www.etcwin.com/", "http://komodoplatform.com/", "http://golem.network/", "http://kiboplatform.net/en/landing.html", "http://decent.ch/", "http://www.synereo.com/", "http://www.lykke.com/", "http://singulardtv.com/", "http://www.iconomi.net/", "http://firstblood.io/sale/", "http://www.antshares.org/", "http://viewfin.com/index.html#team", "http://blockpay.ch/", "http://www.elastic-project.com/", "http://heatledger.com/", "http://www.icoo.io/", "http://rico.xaurum.org/", "http://stratisplatform.com/", "http://www.breakoutcoin.com/", "http://wavesplatform.com/downloads.html#", "http://rise.vision/", "http://getplutons.plutus.it/", "http://wallet.mycelium.com/", "http://forum.daohub.org/", "http://www.project-decorum.com/", "http://ionomy.com/", "http://dgx.io/", "http://www.dgx.io/", "http://lisk.io/", "http://obits.io/", "http://iota.org/", "http://augur.net/", "http://spellsofgenesis.com/", "http://www.factom.com/", "http://www.neucoin.org/en/", "http://dacplay.org/en/", "http://getgems.org", "http://www.museblockchain.com", "http://thesupernet.org/", "http://ethereum.org/", "http://storj.io/index.html", "http://swarmcorp.com/", "http://maidsafe.net/", "http://counterparty.io/"]
def requestLoop(url):
	page = ''
	attempt = 0
	while page == '': 
		try:
		    page = requests.get(url).text
		except:
			print("Attempt ", attempt, " Connection refused by the server..")
			print("Let me sleep for 2 seconds")
			sleep(1)
			print("Was a nice sleep, now let me continue...")
			attempt += 1
			if attempt > 0:
				page = False
			continue
	return page

def listFD(url, ext=''):
	page = requestLoop(url)
	if not page:
		return "N"
	soup = BeautifulSoup(page, 'html.parser')
	for node in soup.find_all('a'):
		print "NODE~ ", node.get('href')
	return [url + node.get('href') for node in soup.find_all('a') if (node.get('href') and node.get('href').endswith(ext))]

pdfarray = {}
for url in urlarray:
	files = []
	print "URL ", url
	listFd = listFD(url, ext)
	if listFD:
		for file in listFD(url, ext):
			files.append(file) 
			print "PDF FILE~~ ", file
			print pdfarray
		pdfarray[url] = files

print "FINAL ARRAY MANE ", pdfarray
