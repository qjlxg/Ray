import requests
from bs4 import BeautifulSoup
from datetime import datetime, timezone
import pytz
import jdatetime

webpage_addresses = [
    "https://t.me/s/v2ray_configs_pool",
    "https://t.me/s/XpnTeam",
    "https://t.me/s/v2rayNGcloud",
    "https://t.me/s/ZibaNabz",
    "https://t.me/s/FreakConfig",
    "https://t.me/s/V_2rey",
    "https://t.me/s/V2ray_Alpha",
    "https://t.me/s/PROXY_MTM",
    "https://t.me/s/SiNABiGO",
    "https://t.me/s/v2rayng12023",
    "https://t.me/s/vlessconfig",
    "https://t.me/s/piazshekan",
    "https://t.me/s/Free_Internet_Iran",
    "https://t.me/s/ARv2ray",
    "https://t.me/s/VPNCUSTOMIZE",
    "https://t.me/s/UnlimitedDev",
    "https://t.me/s/MARAMBASHI",
    "https://t.me/s/PrivateVPNs",
    "https://t.me/s/client_proo",
    "https://t.me/s/nufilter",
    "https://t.me/s/icv2ray",
    "https://t.me/s/Vpn_Mikey",
    "https://t.me/s/v2rayngvpn",
    "https://t.me/s/kingspeedchanel",
    "https://t.me/s/VPN_Xpace",
    "https://t.me/s/SVNTEAM",
    "https://t.me/s/WPSNET",
    "https://t.me/s/AAK_VPN",
"https://t.me/s/ABEDCONFIGPLUSE",
"https://t.me/s/ACCOUNTPLANETIR",
"https://t.me/s/ADAMAK_VPN",
"https://t.me/s/AFV2RAY",
"https://t.me/s/AIFENXIANG2020",
"https://t.me/s/ALFRED_CONFIG",
"https://t.me/s/ALIENVPN402",
"https://t.me/s/ALISMARTVPN",
"https://t.me/s/ALLV2RAY",
"https://t.me/s/ALO_V2RAYNG",
"https://t.me/s/ALSHEYKHVPN",
"https://t.me/s/AMIRINVENTOR2010",
"https://t.me/s/AMIRONETWORK",
"https://t.me/s/AMIRTRONIC",
"https://t.me/s/AMIR_ROOMAN",
"https://t.me/s/AMOFIL",
"https://t.me/s/ANGUS_VPN3",
"https://t.me/s/ANTIFILTERSERVICE",
"https://t.me/s/APPLE_X1",
"https://t.me/s/APPSOONER",
"https://t.me/s/ARGOOO_VPN",
"https://t.me/s/ARGOTAZ",
"https://t.me/s/ARIES_INIT",
"https://t.me/s/ARTAVPN",
"https://t.me/s/ARTEMIS_VPN_FREE",
"https://t.me/s/ARV2RA",
"https://t.me/s/ARV2RAY",
"https://t.me/s/ARYOOVPN",
"https://t.me/s/ASAK_VPN",
"https://t.me/s/ASEEMANVPN",
"https://t.me/s/ASGARD_CONFIG",
"https://t.me/s/ASLIVEEPN",
"https://t.me/s/ASTROVPN_IR",
"https://t.me/s/ASTROVPN_OFFICIAL",
"https://t.me/s/ATLANTICTEAMCHANNEL",
"https://t.me/s/ATOM56778",
"https://t.me/s/ATOVPN",
"https://t.me/s/AUTOFREEVPN",
"https://t.me/s/AVAALVPN",
"https://t.me/s/AWV2RAY",
"https://t.me/s/AXIOSTM",
"https://t.me/s/AXPROXY",
"https://t.me/s/AXV2RAY",
"https://t.me/s/AZADI_AZ_INJA_MIGZARE",
"https://t.me/s/AZADNEIT",
"https://t.me/s/AZAD_INTRNET",
"https://t.me/s/AZARBAYJAB1",
"https://t.me/s/AZURE_V2LESS",
"https://t.me/s/BARAYE2121",
"https://t.me/s/BARAYE3021",
"https://t.me/s/BARAYE_AZADI_INFO",
"https://t.me/s/BARGOVPN",
"https://t.me/s/BEMOLATEXT",
"https://t.me/s/BERICE_V2",
"https://t.me/s/BESTVPN4030",
"https://t.me/s/BETV2RAY",
"https://t.me/s/BIGSMOKE_CONFIG",
"https://t.me/s/BIMNETVPN",
"https://t.me/s/BITNETVPN",
"https://t.me/s/BITNETVPN#BITNET-GIFT",
"https://t.me/s/BLUEBERRYNETWORK",
"https://t.me/s/BLUESHEKAN",
"https://t.me/s/BLUEV2RAYNG",
"https://t.me/s/BLUEVPN_V2RAY",
"https://t.me/s/BMFT1",
"https://t.me/s/BOLBOLVPN",
"https://t.me/s/BORED_VPN",
"https://t.me/s/BPJZX2",
"https://t.me/s/BRIGHT_VPN",
"https://t.me/s/BUFFALO_VPN",
"https://t.me/s/BUG_VPN",
"https://t.me/s/BYPASS_FILTER",
"https://t.me/s/CAA_V2RAY",
"https://t.me/s/CANGURO_ENGLISH",
"https://t.me/s/CAPITAL_NET",
"https://t.me/s/CASSIUSVPN",
"https://t.me/s/CASTOM_V2RAY",
"https://t.me/s/CATTVPN",
"https://t.me/s/CATVPNS",
"https://t.me/s/CAV2RAY",
"https://t.me/s/CCONFIG_V2RAY",
"https://t.me/s/CEPHALON_ALA",
"https://t.me/s/CHANEL_CONFIG",
"https://t.me/s/CHANGE_IP1",
"https://t.me/s/CHV2RAYNP",
"https://t.me/s/CH_A2L",
"https://t.me/s/CIRCLE_VPN",
"https://t.me/s/CISCO_ACC",
"https://t.me/s/CLICK_VPNN",
"https://t.me/s/CLOUDCITYY",
"https://t.me/s/CLUBVPN443",
"https://t.me/s/CLUB_VPN9",
"https://t.me/s/CNFG_V2RAY",
"https://t.me/s/CODVPN",
"https://t.me/s/CONFIGASLI",
"https://t.me/s/CONFIGFORVPN",
"https://t.me/s/CONFIGFORVPN01",
"https://t.me/s/CONFIGMS",
"https://t.me/s/CONFIGPLUSE",
"https://t.me/s/CONFIGPOSITIVE",
"https://t.me/s/CONFIGSCENTER",
"https://t.me/s/CONFIGSSTORE",
"https://t.me/s/CONFIGT",
"https://t.me/s/CONFIGV2RAYFORFREE",
"https://t.me/s/CONFIGV2RAYNG",
"https://t.me/s/CONFIGV2RAY_S",
"https://t.me/s/CONFIG_ON",
"https://t.me/s/CONFIG_PLUS",
"https://t.me/s/CONFIG_PROXY_IR",
"https://t.me/s/CONFINGV2RAAYNG",
"https://t.me/s/CONFING_HUP",
"https://t.me/s/CONFING_PROBLEMS",
"https://t.me/s/CONFING_V2RAYY",
"https://t.me/s/CONNECTBACK",
"https://t.me/s/CONNECTSHU",
"https://t.me/s/CPUVPN",
"https://t.me/s/CUSTOMIZEV2RAY",
"https://t.me/s/CUSTOMV2RAY",
"https://t.me/s/CUSTOMVPNSERVER",
"https://t.me/s/CUSTOM_14",
"https://t.me/s/CUSTOM_CONFIG",
"https://t.me/s/CUSTOM_V2RAY",
"https://t.me/s/DAILYV2RAY",
"https://t.me/s/DAILYV2RY",
"https://t.me/s/DAMONCONFIG",
"https://t.me/s/DARBAZEH_VPN",
"https://t.me/s/DAREDEVILL_404",
"https://t.me/s/DARKMA3TER24",
"https://t.me/s/DARKSECTORA",
"https://t.me/s/DARKTEAM_VPN",
"https://t.me/s/DARKTUNNELVIP1",
"https://t.me/s/DARK_TELECOM",
"https://t.me/s/DASHV2RAY",
"https://t.me/s/DAV2RAY",
"https://t.me/s/DELI_SERVERS",
"https://t.me/s/DERAGV2RAY",
"https://t.me/s/DIAMONDPROXYTM",
"https://t.me/s/DIGIGARD_VPN",
"https://t.me/s/DIGIV2RAY",
"https://t.me/s/DIGIV2RAY23",
"https://t.me/s/DIRECTVPN",
"https://t.me/s/DISCONNECTEDCONFIG",
"https://t.me/s/DNS68",
"https://t.me/s/DONALD_CONFIG",
"https://t.me/s/DRIBBLE7",
"https://t.me/s/DRVPN_NET",
"https://t.me/s/DR_V2RAY",
"https://t.me/s/EASY_FREE_VPN",
"https://t.me/s/EDITORVPN",
"https://t.me/s/EHSAWN8",
"https://t.me/s/ELEUTHERIAVPN",
"https://t.me/s/ELIV2RAY",
"https://t.me/s/ENJECTO",
"https://t.me/s/ERNOXIN_SHOP",
"https://t.me/s/ERTEBATAZAD",
"https://t.me/s/ESIVPP",
"https://t.me/s/EVAY_VPN",
"https://t.me/s/EXOPING",
"https://t.me/s/EXPRESSVPN_420",
"https://t.me/s/EXPRESS_V2RAY",
"https://t.me/s/FALCONPOLV2RAYNG",
"https://t.me/s/FARAHVPN",
"https://t.me/s/FARM_VPN",
"https://t.me/s/FASST_VPN",
"https://t.me/s/FASTFILTERR",
"https://t.me/s/FASTGOZAR",
"https://t.me/s/FASTKANFIG",
"https://t.me/s/FASTVPNORUMMOBILE",
"https://t.me/s/FAST_2RAY",
"https://t.me/s/FATI_FFX",
"https://t.me/s/FERI_V2RAY_PROXY",
"https://t.me/s/FILTER5050",
"https://t.me/s/FILTERINTL",
"https://t.me/s/FILTERK0SH",
"https://t.me/s/FILTEROGHORTBEDE",
"https://t.me/s/FILTERSHEKAN_CHANNEL",
"https://t.me/s/FILTERZAPATA",
"https://t.me/s/FIREWALLVPN",
"https://t.me/s/FIRE_VPN_CHANNEL",
"https://t.me/s/FIX_PROXY",
"https://t.me/s/FLASH_PROXIES",
"https://t.me/s/FLOTGUARD",
"https://t.me/s/FLYV2RAY",
"https://t.me/s/FNET00",
"https://t.me/s/FOXNT",
"https://t.me/s/FREAKCONFIG",
"https://t.me/s/FREE4ALLVPN",
"https://t.me/s/FREECONFING",
"https://t.me/s/FREEDOMNETOFFICIAL",
"https://t.me/s/FREEDOM_CONFIG",
"https://t.me/s/FREEIRANWEB",
"https://t.me/s/FREENAPSTERNETV",
"https://t.me/s/FREENETPRO99",
"https://t.me/s/FREEOWNVPN",
"https://t.me/s/FREESHADOWSOCK",
"https://t.me/s/FREESTRONGVPN",
"https://t.me/s/FREEV2FLYNG",
"https://t.me/s/FREEV2RAY2024",
"https://t.me/s/FREEV2RAYM",
"https://t.me/s/FREEV2RAYS",
"https://t.me/s/FREEV2RAYSSR",
"https://t.me/s/FREEVMESS",
"https://t.me/s/FREEVPN3327",
"https://t.me/s/FREEVPNCHINA",
"https://t.me/s/FREEVPNHOMESCONFIGS",
"https://t.me/s/FREE_INTERNETE_IRAN",
"https://t.me/s/FREE_INTERNET_IRAN",
"https://t.me/s/FREE_OMEGA",
"https://t.me/s/FREE_PROXY_001",
"https://t.me/s/FREE_SHEKAN",
"https://t.me/s/FREE_V2RAYYY",
"https://t.me/s/FREE_VPN02",
"https://t.me/s/FREE_WORLLD",
"https://t.me/s/FREV2RAYNG",
"https://t.me/s/FSV2RAY",
"https://t.me/s/FUNIX_SHOPE",
"https://t.me/s/FV2RAY",
"https://t.me/s/GANGSTER_VPN",
"https://t.me/s/GARNET_FREE",
"https://t.me/s/GE2RAY",
"https://t.me/s/GETANYMESSAGECHANNEL",
"https://t.me/s/GETCONFIGIR",
"https://t.me/s/GH_V2RAYNG",
"https://t.me/s/GIGI_VPN_VIP",
"https://t.me/s/GIVEVPN",
"https://t.me/s/GOLDD_V2RAY",
"https://t.me/s/GOLDENSHIINEVPN",
"https://t.me/s/GOLDEN_VPN_OFFICIAL",
"https://t.me/s/GOLESTAN_VPN",
"https://t.me/s/GOLF_VPN",
"https://t.me/s/GOZARGAHVPN",
"https://t.me/s/GOZARGAH_AZADI",
"https://t.me/s/GRIZZLYVPN",
"https://t.me/s/GV2RAY",
"https://t.me/s/HAJIMAMADVPN",
"https://t.me/s/HAMSTER_VPNN",
"https://t.me/s/HATUNNEL_VPN",
"https://t.me/s/HEINUHOME",
"https://t.me/s/HELIX_SERVERS",
"https://t.me/s/HENNESSYPRO",
"https://t.me/s/HERCULESL_SERVER",
"https://t.me/s/HERMANOSVPN",
"https://t.me/s/HIVEPING",
"https://t.me/s/HKAA0",
"https://t.me/s/HOLOGATE6",
"https://t.me/s/HOOSHANG_VPN1",
"https://t.me/s/HOPEV2RAY",
"https://t.me/s/HOPE_NET",
"https://t.me/s/HOSSEINSTORE_ZA",
"https://t.me/s/HOT_V2RY",
"https://t.me/s/HPV2RAY",
"https://t.me/s/HPV2RAYNG",
"https://t.me/s/HPV2RAY_OFFICIAL",
"https://t.me/s/HTTP_INJECTOR99",
"https://t.me/s/HYPERVPNS",
"https://t.me/s/Hope_Net",
"https://t.me/s/I3V2RAY",
"https://t.me/s/IBV2RAY",
"https://t.me/s/ICLOUDYSHOP",
"https://t.me/s/ICV2RAY",
"https://t.me/s/IGRSDET",
"https://t.me/s/IMRV2RAY",
"https://t.me/s/INFO_2IT_CHANNEL",
"https://t.me/s/INJECTORMCONF",
"https://t.me/s/INJECTORSAZAN",
"https://t.me/s/INTERNET4IRAN",
"https://t.me/s/INTERNET_NOR",
"https://t.me/s/IPHONEBAX",
"https://t.me/s/IPPSCANCONFIG",
"https://t.me/s/IPV2RAY",
"https://t.me/s/IPV2RAYNG",
"https://t.me/s/IP_CF",
"https://t.me/s/IP_CF_CONFIG",
"https://t.me/s/IP_RAMZI",
"https://t.me/s/IRANBAXVPN",
"https://t.me/s/IRANBFILTER",
"https://t.me/s/IRANIV2RAY",
"https://t.me/s/IRANMEDICALVPN",
"https://t.me/s/IRANPROXYPRO",
"https://t.me/s/IRANVIPNET",
"https://t.me/s/IRAN_MEHR_VPN",
"https://t.me/s/IRAN_V2R",
"https://t.me/s/IRAN_V2RAY1",
"https://t.me/s/IRNV2RAY",
"https://t.me/s/IRONNETT",
"https://t.me/s/IROV2RAYN",
"https://t.me/s/IR_CONFIG_AN",
"https://t.me/s/IR_NETPROXY",
"https://t.me/s/IR_PROXYV2RAY",
"https://t.me/s/IR_VPNS",
"https://t.me/s/ITV2RAY",
"https://t.me/s/JAVID_IRAN_VPN",
"https://t.me/s/JCVPN",
"https://t.me/s/JEDAL_VPN",
"https://t.me/s/JETUPNET",
"https://t.me/s/JIEDIANF",
"https://t.me/s/JIEDIANSSR",
"https://t.me/s/JIUJIED",
"https://t.me/s/JOKERV2RAY",
"https://t.me/s/KABIRVPN",
"https://t.me/s/KAFING_2",
"https://t.me/s/KAKAYA3IN",
"https://t.me/s/KHP_PREMIUM_KEY",
"https://t.me/s/KILID_STOR",
"https://t.me/s/KINGOFV2RAY",
"https://t.me/s/KUTO_PROXY",
"https://t.me/s/KUTO_PROXY2",
"https://t.me/s/LAKVPN1",
"https://t.me/s/LEGENDERY_SERVER",
"https://t.me/s/LIGHTNING6",
"https://t.me/s/LIQ_VPN",
"https://t.me/s/LOCKEY_VPN",
"https://t.me/s/LRNBYMAA",
"https://t.me/s/MAHDIVPN2",
"https://t.me/s/MT_TEAM_IRAN",
"https://t.me/s/NETGUARDSTORE",
"https://t.me/s/NPV_V2RAY",
"https://t.me/s/NUFILTER",
"https://t.me/s/OUTLINEIRAN",
"https://t.me/s/PROXY_MTM",
"https://t.me/s/PR_GUARD",
"https://t.me/s/ROMAX_VPN",
"https://t.me/s/SABZ_V2RAY",
"https://t.me/s/SAVTEAM",
"https://t.me/s/SRCVPN",
"https://t.me/s/STAR_HACK_100",
"https://t.me/s/ServerNett",
"https://t.me/s/TEHRANARGO",
"https://t.me/s/TIKTOK_PROXY",
"https://t.me/s/TOYOTA_PROXYYYY",
"https://t.me/s/V2FETCH",
"https://t.me/s/V2FRE",
"https://t.me/s/V2HAMID",
"https://t.me/s/V2NET_IRAN",
"https://t.me/s/V2RAYN2G",
"https://t.me/s/V2RAYNG_VPNT",
"https://t.me/s/V2RRAY_NG",
"https://t.me/s/V2TRY_55",
"https://t.me/s/VPN707",
"https://t.me/s/VPNAMOHELP",
"https://t.me/s/VPNETI",
"https://t.me/s/VPNFREEO",
"https://t.me/s/VPNHUB69",
"https://t.me/s/VPNMEGA1",
"https://t.me/s/VPNTAKO",
"https://t.me/s/VPN_CONNECT",
"https://t.me/s/VPN_ROOM",
"https://t.me/s/VPN_SHOP_V1",
"https://t.me/s/WSBVPN",
"https://t.me/s/XNXV2RAY",
"https://t.me/s/ZED_VPN",
"https://t.me/s/aak_vpn",
"https://t.me/s/abedconfigpluse",
"https://t.me/s/accountplanetir",
"https://t.me/s/adamak_vpn",
"https://t.me/s/afv2ray",
"https://t.me/s/aifenxiang2020",
"https://t.me/s/alfred_config",
"https://t.me/s/alienvpn402",
"https://t.me/s/allv2ray",
"https://t.me/s/alo_v2rayng",
"https://t.me/s/alsheykhvpn",
"https://t.me/s/amir_rooman",
"https://t.me/s/amirinventor2010",
"https://t.me/s/amironetwork",
"https://t.me/s/amirtronic",
"https://t.me/s/amofil",
"https://t.me/s/antifilterservice",
"https://t.me/s/appsooner",
"https://t.me/s/argotaz",
"https://t.me/s/aries_init",
"https://t.me/s/arv2ray",
"https://t.me/s/aryoovpn",
"https://t.me/s/asak_vpn",
"https://t.me/s/asgard_config",
"https://t.me/s/asliveepn",
"https://t.me/s/asrnovin_ir",
"https://t.me/s/astrovpn_official",
"https://t.me/s/atovpn",
"https://t.me/s/avaalvpn",
"https://t.me/s/awv2ray",
"https://t.me/s/axiostm",
"https://t.me/s/axproxy",
"https://t.me/s/azad_intrnet",
"https://t.me/s/azadi_az_inja_migzare",
"https://t.me/s/azarbayjab1",
"https://t.me/s/azure_v2less",
"https://t.me/s/baraye2121",
"https://t.me/s/baraye3021",
"https://t.me/s/bargovpn",
"https://t.me/s/berice_v2",
"https://t.me/s/bestvpn4030",
"https://t.me/s/betv2ray",
"https://t.me/s/bigsmoke_config",
"https://t.me/s/bimnetvpn",
"https://t.me/s/bitnetvpn",
"https://t.me/s/blueberrynetwork",
"https://t.me/s/blueshekan",
"https://t.me/s/bluev2rayng",
"https://t.me/s/bluevpn_v2ray",
"https://t.me/s/bored_vpn",
"https://t.me/s/bpjzx2",
"https://t.me/s/buffalo_vpn",
"https://t.me/s/bug_vpn",
"https://t.me/s/bypass_filter",
"https://t.me/s/caa_v2ray",
"https://t.me/s/capital_net",
"https://t.me/s/cassiusvpn",
"https://t.me/s/cattvpn",
"https://t.me/s/catvpns",
"https://t.me/s/cav2ray",
"https://t.me/s/cconfig_v2ray",
"https://t.me/s/cephalon_ala",
"https://t.me/s/ch_a2l",
"https://t.me/s/change_ip1",
"https://t.me/s/chatbuzzteam",
"https://t.me/s/chv2raynp",
"https://t.me/s/circle_vpn",
"https://t.me/s/click_vpnn",
"https://t.me/s/cloudcityy",
"https://t.me/s/club_vpn9",
"https://t.me/s/clubvpn443",
"https://t.me/s/cnfg_v2ray",
"https://t.me/s/codvpn",
"https://t.me/s/config_on",
"https://t.me/s/config_plus",
"https://t.me/s/config_proxy_ir",
"https://t.me/s/configasli",
"https://t.me/s/configforvpn",
"https://t.me/s/configms",
"https://t.me/s/configpositive",
"https://t.me/s/configt",
"https://t.me/s/configv2rayforfree",
"https://t.me/s/configv2rayng",
"https://t.me/s/confing_hup",
"https://t.me/s/confing_problems",
"https://t.me/s/confing_v2rayy",
"https://t.me/s/confingv2raayng",
"https://t.me/s/connectback",
"https://t.me/s/connectshu",
"https://t.me/s/cpuvpn",
"https://t.me/s/custom_14",
"https://t.me/s/custom_config",
"https://t.me/s/custom_v2ray",
"https://t.me/s/customizev2ray",
"https://t.me/s/customv2ray",
"https://t.me/s/customvpnserver",
"https://t.me/s/dailyv2ray",
"https://t.me/s/damonconfig",
"https://t.me/s/darbazeh_vpn",
"https://t.me/s/daredevill_404",
"https://t.me/s/dark_telecom",
"https://t.me/s/darkma3ter24",
"https://t.me/s/darkteam_vpn",
"https://t.me/s/darktunnelvip1",
"https://t.me/s/dashv2ray",
"https://t.me/s/dav2ray",
"https://t.me/s/deragv2ray",
"https://t.me/s/digiv2ray",
"https://t.me/s/digiv2ray23",
"https://t.me/s/directvpn",
"https://t.me/s/disconnectedconfig",
"https://t.me/s/dns68",
"https://t.me/s/drvpn_net",
"https://t.me/s/easy_free_vpn",
"https://t.me/s/ehsawn8",
"https://t.me/s/eleutheriavpn",
"https://t.me/s/eliv2ray",
"https://t.me/s/enjecto",
"https://t.me/s/ernoxin_shop",
"https://t.me/s/ertebatazad",
"https://t.me/s/esivpp",
"https://t.me/s/evay_vpn",
"https://t.me/s/exoping",
"https://t.me/s/express_v2ray",
"https://t.me/s/expressvpn_420",
"https://t.me/s/falconpolv2rayng",
"https://t.me/s/farahvpn",
"https://t.me/s/farm_vpn",
"https://t.me/s/fasst_vpn",
"https://t.me/s/fast_2ray",
"https://t.me/s/fastfilterr",
"https://t.me/s/fastgozar",
"https://t.me/s/fastkanfig",
"https://t.me/s/fastvpnorummobile",
"https://t.me/s/fati_ffx",
"https://t.me/s/feri_v2ray_proxy",
"https://t.me/s/filter5050",
"https://t.me/s/filterintl",
"https://t.me/s/filterk0sh",
"https://t.me/s/filteroghortbede",
"https://t.me/s/filterzapata",
"https://t.me/s/fire_vpn_channel",
"https://t.me/s/flotguard",
"https://t.me/s/flyv2ray",
"https://t.me/s/fnet00",
"https://t.me/s/freakconfig",
"https://t.me/s/free_internete_iran",
"https://t.me/s/free_omega",
"https://t.me/s/free_shekan",
"https://t.me/s/free_v2rayyy",
"https://t.me/s/free_vpn02",
"https://t.me/s/free_worlld",
"https://t.me/s/freeconfing",
"https://t.me/s/freedom_config",
"https://t.me/s/freeiranweb",
"https://t.me/s/freenapsternetv",
"https://t.me/s/freenetpro99",
"https://t.me/s/freestrongvpn",
"https://t.me/s/freev2ray2024",
"https://t.me/s/freev2raym",
"https://t.me/s/freevmess",
"https://t.me/s/frev2rayng",
"https://t.me/s/fsv2ray",
"https://t.me/s/fv2ray",
"https://t.me/s/gangster_vpn",
"https://t.me/s/garnet_free",
"https://t.me/s/ge2ray",
"https://t.me/s/getconfigir",
"https://t.me/s/gh_v2rayng",
"https://t.me/s/gigi_vpn_vip",
"https://t.me/s/givevpn",
"https://t.me/s/goldd_v2ray",
"https://t.me/s/golden_vpn_official",
"https://t.me/s/goldenshiinevpn",
"https://t.me/s/golestan_vpn",
"https://t.me/s/gozargah_azadi",
"https://t.me/s/gozargahvpn",
"https://t.me/s/grizzlyvpn",
"https://t.me/s/gv2ray",
"https://t.me/s/hajimamadvpn",
"https://t.me/s/hamster_vpnn",
"https://t.me/s/hatunnel_vpn",
"https://t.me/s/helix_servers",
"https://t.me/s/hennessypro",
"https://t.me/s/herculesl_server",
"https://t.me/s/hiveping",
"https://t.me/s/hkaa0",
"https://t.me/s/hope_net",
"https://t.me/s/hopev2ray",
"https://t.me/s/hosseinstore_za",
"https://t.me/s/hot_v2ry",
"https://t.me/s/hpv2ray",
"https://t.me/s/hpv2ray_official",
"https://t.me/s/hpv2rayng",
"https://t.me/s/http_injector99",
"https://t.me/s/hypervpns",
"https://t.me/s/i3v2ray",
"https://t.me/s/ibv2ray",
"https://t.me/s/icloudyshop",
"https://t.me/s/icv2ray",
"https://t.me/s/igrsdet",
"https://t.me/s/imrv2ray",
"https://t.me/s/info_2it_channel",
"https://t.me/s/injectormconf",
"https://t.me/s/injectorsazan",
"https://t.me/s/internet_nor",
"https://t.me/s/ip_cf",
"https://t.me/s/ip_ramzi",
"https://t.me/s/ippscanconfig",
"https://t.me/s/ipv2ray",
"https://t.me/s/ipv2rayng",
"https://t.me/s/ir_netproxy",
"https://t.me/s/ir_proxyv2ray",
"https://t.me/s/iran_access",
"https://t.me/s/iran_mehr_vpn",
"https://t.me/s/iran_v2r",
"https://t.me/s/iran_v2ray1",
"https://t.me/s/iranbaxvpn",
"https://t.me/s/iranbfilter",
"https://t.me/s/iraniv2ray",
"https://t.me/s/iranmedicalvpn",
"https://t.me/s/iranproxypro",
"https://t.me/s/iranvipnet",
"https://t.me/s/irnv2ray",
"https://t.me/s/ironnett",
"https://t.me/s/irov2rayn",
"https://t.me/s/isvvpn",
"https://t.me/s/itv2ray",
"https://t.me/s/javid_iran_vpn",
"https://t.me/s/jd_vpn",
"https://t.me/s/jedal_vpn",
"https://t.me/s/jetupnet",
"https://t.me/s/jetvpnv",
"https://t.me/s/jokerv2ray",
"https://t.me/s/kabirvpn",
"https://t.me/s/kafing_2",
"https://t.me/s/kakaya3in",
"https://t.me/s/kesslervpn",
"https://t.me/s/kiava",
"https://t.me/s/kilid_stor",
"https://t.me/s/kingofilter",
"https://t.me/s/kingofv2ray",
"https://t.me/s/kingspeedchanel",
"https://t.me/s/kinsta_service",
"https://t.me/s/kurd_v2ray",
"https://t.me/s/kurdvpn1",
"https://t.me/s/kuto_proxy",
"https://t.me/s/kuto_proxy2",
"https://t.me/s/lakvpn1",
"https://t.me/s/legendery_server",
"https://t.me/s/lemonshopvpn",
"https://t.me/s/lepingvpn",
"https://t.me/s/lexa_vpn",
"https://t.me/s/lightning6",
"https://t.me/s/lion_channel_vpn",
"https://t.me/s/liquidproxy",
"https://t.me/s/litevp",
"https://t.me/s/loatvpn",
"https://t.me/s/lockey_vpn",
"https://t.me/s/lrnbymaa",
"https://t.me/s/lusty_queen_vpn",
"https://t.me/s/m_vipv2ray",
"https://t.me/s/mahdish0p",
"https://t.me/s/mahdivpn2",
"https://t.me/s/mainv2ray",
"https://t.me/s/manzariyeh_rasht",
"https://t.me/s/maradona_vpn",
"https://t.me/s/marzazad",
"https://t.me/s/mastervpnshop1",
"https://t.me/s/mater_1345",
"https://t.me/s/maxvpnc",
"https://t.me/s/maznet",
"https://t.me/s/mehrosaboran",
"https://t.me/s/meli_prooxy",
"https://t.me/s/meli_proxyy",
"https://t.me/s/meli_proxyyy",
"https://t.me/s/meli_v2rayng",
"https://t.me/s/melov2ray",
"https://t.me/s/mester_v2ray",
"https://t.me/s/metaanet",
"https://t.me/s/mftizi",
"https://t.me/s/mgvpnsale",
"https://t.me/s/mi_pn_official",
"https://t.me/s/migping",
"https://t.me/s/mikasavpn",
"https://t.me/s/mimitdl",
"https://t.me/s/minovpnch",
"https://t.me/s/miov2ray",
"https://t.me/s/moft_vpn",
"https://t.me/s/moftinet",
"https://t.me/s/mohammad_i_t",
"https://t.me/s/moiinmk",
"https://t.me/s/mrclud",
"https://t.me/s/mrv2raay",
"https://t.me/s/mrv2ray",
"https://t.me/s/mrvpn1403",
"https://t.me/s/msv2flyng",
"https://t.me/s/msv2raynp",
"https://t.me/s/mt_team_iran",
"https://t.me/s/mtconfig",
"https://t.me/s/mtproto_666",
"https://t.me/s/mtpv2ray",
"https://t.me/s/mxv2ray",
"https://t.me/s/myvpn98",
"https://t.me/s/n1xv2ray",
"https://t.me/s/n2vpn",
"https://t.me/s/napoliii1994",
"https://t.me/s/napsternetv_ir",
"https://t.me/s/napsternetvirani",
"https://t.me/s/narcod_ping",
"https://t.me/s/nepo_v2ray",
"https://t.me/s/net_azad_1",
"https://t.me/s/netazadchannel",
"https://t.me/s/netfreedom0",
"https://t.me/s/netguardstore",
"https://t.me/s/netmellianti",
"https://t.me/s/netspeedservice",
"https://t.me/s/new_proxy_channel",
"https://t.me/s/next_serverpanel",
"https://t.me/s/nicolv2ray",
"https://t.me/s/nim_ping",
"https://t.me/s/nitrovpne",
"https://t.me/s/nn_vpn",
"https://t.me/s/nodes_share",
"https://t.me/s/nofiltering2",
"https://t.me/s/noforcedheaven",
"https://t.me/s/nordaccount1",
"https://t.me/s/novinology",
"https://t.me/s/npv_v2ray",
"https://t.me/s/nufilter",
"https://t.me/s/offlinenet",
"https://t.me/s/ognett",
"https://t.me/s/ohvpn",
"https://t.me/s/omegavp",
"https://t.me/s/optvpn",
"https://t.me/s/otana_vpn",
"https://t.me/s/outline_ir",
"https://t.me/s/outline_oneclick1",
"https://t.me/s/outlineiran",
"https://t.me/s/outlines_vpn",
"https://t.me/s/outlinev",
"https://t.me/s/outlinevpnofficial",
"https://t.me/s/ovpn2",
"https://t.me/s/oxir_vpn",
"https://t.me/s/oxnet_ir",
"https://t.me/s/pak4you",
"https://t.me/s/pandasng",
"https://t.me/s/pardazeshvpn",
"https://t.me/s/pars_vpn3",
"https://t.me/s/parsashonam",
"https://t.me/s/parsconfigg",
"https://t.me/s/parsv2ray1",
"https://t.me/s/parsvip0",
"https://t.me/s/persian_proxy6",
"https://t.me/s/perv2ray",
"https://t.me/s/phoenix_ti",
"https://t.me/s/piavpngo",
"https://t.me/s/ping01pro",
"https://t.me/s/polproxy",
"https://t.me/s/pov2ray",
"https://t.me/s/pr_guard",
"https://t.me/s/private_access_guard_vpn",
"https://t.me/s/privatevpnn",
"https://t.me/s/privatevpns",
"https://t.me/s/prooxyk",
"https://t.me/s/proprojec",
"https://t.me/s/proserverstm",
"https://t.me/s/proxie",
"https://t.me/s/proxiiraniii",
"https://t.me/s/proxy48",
"https://t.me/s/proxy_kafee",
"https://t.me/s/proxy_mtm",
"https://t.me/s/proxy_n1",
"https://t.me/s/proxy_shadosocks",
"https://t.me/s/proxy_v2box",
"https://t.me/s/proxycityiran",
"https://t.me/s/proxyfn",
"https://t.me/s/proxyforopeta",
"https://t.me/s/proxyfull",
"https://t.me/s/proxyhubc",
"https://t.me/s/proxyirancel",
"https://t.me/s/proxystore11",
"https://t.me/s/proxysudo",
"https://t.me/s/proxyvpnvip",
"https://t.me/s/proxyymeliii",
"https://t.me/s/puni_shop_v2rayng",
"https://t.me/s/pusyvpn",
"https://t.me/s/pydriclub",
"https://t.me/s/qafor_1",
"https://t.me/s/qand_shecan",
"https://t.me/s/qeshmserver",
"https://t.me/s/qrv2ray",
"https://t.me/s/qvpnn",
"https://t.me/s/rayanconf",
"https://t.me/s/realvpnmaster",
"https://t.me/s/red2ray",
"https://t.me/s/renetvpn",
"https://t.me/s/rezaw_server",
"https://t.me/s/rk_filtershking",
"https://t.me/s/rnrifci",
"https://t.me/s/romax_vpn",
"https://t.me/s/s0013_official",
"https://t.me/s/sabz_v2ray",
"https://t.me/s/samiv2ray",
"https://t.me/s/satafkompani",
"https://t.me/s/satellitenewspersian",
"https://t.me/s/satoshivpn",
"https://t.me/s/savagev2ray",
"https://t.me/s/savteam",
"https://t.me/s/securit_y_breach",
"https://t.me/s/selinc",
"https://t.me/s/server_housing03",
"https://t.me/s/server_nekobox",
"https://t.me/s/serverii",
"https://t.me/s/servernett",
"https://t.me/s/serversiran11",
"https://t.me/s/serverv2ray00",
"https://t.me/s/seven_ping",
"https://t.me/s/sevenvpnchannel",
"https://t.me/s/shadowproxy66",
"https://t.me/s/shadowsockskeys",
"https://t.me/s/shconfig",
"https://t.me/s/shh_proxy",
"https://t.me/s/shopzonix",
"https://t.me/s/sifev2ray",
"https://t.me/s/sinamobail",
"https://t.me/s/sitefilter",
"https://t.me/s/skivpn",
"https://t.me/s/sobi_vpn",
"https://t.me/s/socks5tobefree",
"https://t.me/s/sorenaa_vpn",
"https://t.me/s/special_net8",
"https://t.me/s/spikevpn",
"https://t.me/s/srcvpn",
"https://t.me/s/srv2ray",
"https://t.me/s/standvpn",
"https://t.me/s/star_hack_100",
"https://t.me/s/starv2rayn",
"https://t.me/s/summertimeus",
"https://t.me/s/superpinghub",
"https://t.me/s/superv2rang",
"https://t.me/s/tawanaclub",
"https://t.me/s/tc_v2ray",
"https://t.me/s/tehranargo",
"https://t.me/s/tehranfreevpn",
"https://t.me/s/tehron98",
"https://t.me/s/teiknovpn",
"https://t.me/s/telmavpn",
"https://t.me/s/thunderv2ray",
"https://t.me/s/tigervpn_free",
"https://t.me/s/tiktok_proxy",
"https://t.me/s/tiny_vpn_official",
"https://t.me/s/titan_v2rayvpn",
"https://t.me/s/tizjo",
"https://t.me/s/tls_v2ray",
"https://t.me/s/tokyonetwork",
"https://t.me/s/torang_vpn",
"https://t.me/s/tov2rayy",
"https://t.me/s/toyota_proxy",
"https://t.me/s/trand_farsi",
"https://t.me/s/turboo_server",
"https://t.me/s/tv2rayrr",
"https://t.me/s/tv_v2ray",
"https://t.me/s/typevpn",
"https://t.me/s/ultrasurf_12",
"https://t.me/s/uniquenett",
"https://t.me/s/unlimiteddev",
"https://t.me/s/uraniumvpn",
"https://t.me/s/uvpn_org",
"https://t.me/s/uvpnir",
"https://t.me/s/v2_city",
"https://t.me/s/v2_fast",
"https://t.me/s/v2_hub",
"https://t.me/s/v2aboo",
"https://t.me/s/v2advicr",
"https://t.me/s/v2aryng_vpn",
"https://t.me/s/v2boxng74",
"https://t.me/s/v2conf",
"https://t.me/s/v2configer",
"https://t.me/s/v2fetch",
"https://t.me/s/v2fre",
"https://t.me/s/v2freenet",
"https://t.me/s/v2graphy",
"https://t.me/s/v2hamid",
"https://t.me/s/v2kingfree",
"https://t.me/s/v2line",
"https://t.me/s/v2meowcf",
"https://t.me/s/v2mod",
"https://t.me/s/v2naptv",
"https://t.me/s/v2net_iran",
"https://t.me/s/v2org",
"https://t.me/s/v2pedia",
"https://t.me/s/v2power",
"https://t.me/s/v2ra2",
"https://t.me/s/v2raand",
"https://t.me/s/v2raayngconfig",
"https://t.me/s/v2rang_255",
"https://t.me/s/v2range",
"https://t.me/s/v2ray1000",
"https://t.me/s/v2ray16",
"https://t.me/s/v2ray1_ng",
"https://t.me/s/v2ray1ran",
"https://t.me/s/v2ray24",
"https://t.me/s/v2ray4win",
"https://t.me/s/v2ray6388",
"https://t.me/s/v2ray96",
"https://t.me/s/v2ray_83",
"https://t.me/s/v2ray_alpha",
"https://t.me/s/v2ray_alpha07",
"https://t.me/s/v2ray_best_iran",
"https://t.me/s/v2ray_bro",
"https://t.me/s/v2ray_cartel",
"https://t.me/s/v2ray_configs_pool",
"https://t.me/s/v2ray_donya",
"https://t.me/s/v2ray_fark",
"https://t.me/s/v2ray_for_free",
"https://t.me/s/v2ray_god",
"https://t.me/s/v2ray_melli",
"https://t.me/s/v2ray_n",
"https://t.me/s/v2ray_napster_vpn",
"https://t.me/s/v2ray_ng",
"https://t.me/s/v2ray_ng_vip",
"https://t.me/s/v2ray_npv",
"https://t.me/s/v2ray_official",
"https://t.me/s/v2ray_only_free",
"https://t.me/s/v2ray_raha",
"https://t.me/s/v2ray_raimon",
"https://t.me/s/v2ray_reality_new",
"https://t.me/s/v2ray_rh",
"https://t.me/s/v2ray_rolly",
"https://t.me/s/v2ray_shopb",
"https://t.me/s/v2ray_sos",
"https://t.me/s/v2ray_string",
"https://t.me/s/v2ray_sub",
"https://t.me/s/v2ray_swhil",
"https://t.me/s/v2ray_team",
"https://t.me/s/v2ray_ty",
"https://t.me/s/v2ray_vemo",
"https://t.me/s/v2ray_vmes",
"https://t.me/s/v2ray_vpn_free",
"https://t.me/s/v2ray_vpna",
"https://t.me/s/v2ray_youtube",
"https://t.me/s/v2rayaliw",
"https://t.me/s/v2rayargon",
"https://t.me/s/v2rayarmy",
"https://t.me/s/v2raybest1",
"https://t.me/s/v2raych",
"https://t.me/s/v2raychanel",
"https://t.me/s/v2raycrow",
"https://t.me/s/v2raydiyako",
"https://t.me/s/v2rayexpress",
"https://t.me/s/v2rayfa",
"https://t.me/s/v2rayfast",
"https://t.me/s/v2rayfast_7",
"https://t.me/s/v2rayfree",
"https://t.me/s/v2rayfree1",
"https://t.me/s/v2raygofree",
"https://t.me/s/v2rayhubvip",
"https://t.me/s/v2rayi_net",
"https://t.me/s/v2raying",
"https://t.me/s/v2rayland02",
"https://t.me/s/v2raylandd",
"https://t.me/s/v2rayliberty",
"https://t.me/s/v2raymakers",
"https://t.me/s/v2raymastermind",
"https://t.me/s/v2rayn2g",
"https://t.me/s/v2rayn_config",
"https://t.me/s/v2rayng116",
"https://t.me/s/v2rayng12023",
"https://t.me/s/v2rayng14",
"https://t.me/s/v2rayng20000000",
"https://t.me/s/v2rayng3",
"https://t.me/s/v2rayng_13",
"https://t.me/s/v2rayng_147",
"https://t.me/s/v2rayng_81",
"https://t.me/s/v2rayng_aads",
"https://t.me/s/v2rayng_account_free",
"https://t.me/s/v2rayng_active",
"https://t.me/s/v2rayng_anti",
"https://t.me/s/v2rayng_city",
"https://t.me/s/v2rayng_coonfig",
"https://t.me/s/v2rayng_ip",
"https://t.me/s/v2rayng_lion",
"https://t.me/s/v2rayng_madam",
"https://t.me/s/v2rayng_nv",
"https://t.me/s/v2rayng_nv1",
"https://t.me/s/v2rayng_nvvpn",
"https://t.me/s/v2rayng_outline_vpn",
"https://t.me/s/v2rayng_outlinee",
"https://t.me/s/v2rayng_sell",
"https://t.me/s/v2rayng_serverr1",
"https://t.me/s/v2rayng_vpn",
"https://t.me/s/v2rayng_vpnn",
"https://t.me/s/v2rayng_vpnorg",
"https://t.me/s/v2rayng_vpnt",
"https://t.me/s/v2rayngalpha",
"https://t.me/s/v2rayngalphagamer",
"https://t.me/s/v2rayngc",
"https://t.me/s/v2rayngchaannel",
"https://t.me/s/v2rayngcloud",
"https://t.me/s/v2rayngconfiig",
"https://t.me/s/v2rayngconfings",
"https://t.me/s/v2rayngfreee",
"https://t.me/s/v2rayngg_iran",
"https://t.me/s/v2rayngim",
"https://t.me/s/v2rayngn",
"https://t.me/s/v2rayngninja",
"https://t.me/s/v2rayngraisi",
"https://t.me/s/v2rayngrit",
"https://t.me/s/v2rayngseven",
"https://t.me/s/v2rayngup",
"https://t.me/s/v2rayngv",
"https://t.me/s/v2rayngvp",
"https://t.me/s/v2rayngvpn_1",
"https://t.me/s/v2rayngvpnn",
"https://t.me/s/v2rayngvvpn",
"https://t.me/s/v2rayngzendegimamad",
"https://t.me/s/v2raynselling",
"https://t.me/s/v2rayo7ybv67i76",
"https://t.me/s/v2rayopen",
"https://t.me/s/v2rayorng",
"https://t.me/s/v2raypanelhub",
"https://t.me/s/v2rayping",
"https://t.me/s/v2rayport",
"https://t.me/s/v2rayprooo",
"https://t.me/s/v2rayprotocol",
"https://t.me/s/v2rayrb6",
"https://t.me/s/v2rayserverfreenet",
"https://t.me/s/v2rayshop_m",
"https://t.me/s/v2rayspeed",
"https://t.me/s/v2raystudents",
"https://t.me/s/v2raytg",
"https://t.me/s/v2rayturbo",
"https://t.me/s/v2raytz",
"https://t.me/s/v2rayvmess",
"https://t.me/s/v2rayvpn2",
"https://t.me/s/v2rayvpnclub",
"https://t.me/s/v2rayvpnking0",
"https://t.me/s/v2rayvx",
"https://t.me/s/v2rayweb",
"https://t.me/s/v2rayy_ir",
"https://t.me/s/v2rayy_vpn13",
"https://t.me/s/v2rayyngvpn",
"https://t.me/s/v2rayza",
"https://t.me/s/v2rayzone",
"https://t.me/s/v2reyy",
"https://t.me/s/v2rez",
"https://t.me/s/v2riran",
"https://t.me/s/v2roay",
"https://t.me/s/v2rplus",
"https://t.me/s/v2rray1_ng",
"https://t.me/s/v2rray_ng",
"https://t.me/s/v2ry_proxy",
"https://t.me/s/v2ryng01",
"https://t.me/s/v2ryng_vpn",
"https://t.me/s/v2ryngfree",
"https://t.me/s/v2ryvip",
"https://t.me/s/v2safe",
"https://t.me/s/v2safee",
"https://t.me/s/v2servers1",
"https://t.me/s/v2sezar",
"https://t.me/s/v2shop2",
"https://t.me/s/v3410ray",
"https://t.me/s/v5ray_ng",
"https://t.me/s/v_2ray1",
"https://t.me/s/v_2rayng0",
"https://t.me/s/v_2rayngvpn",
"https://t.me/s/v_2rayy_ng",
"https://t.me/s/v_p_lv",
"https://t.me/s/vboxpanel",
"https://t.me/s/vc_proxy",
"https://t.me/s/vein_vpn",
"https://t.me/s/vemessvpn",
"https://t.me/s/vipfastspeed",
"https://t.me/s/vipv2rayn",
"https://t.me/s/vipv2rayngnp",
"https://t.me/s/vipv2rayngvip",
"https://t.me/s/vipv2rayvip",
"https://t.me/s/vipv2rey",
"https://t.me/s/vipvpn_v2ray",
"https://t.me/s/virapn",
"https://t.me/s/virav2ray",
"https://t.me/s/vistav2ray",
"https://t.me/s/vless1",
"https://t.me/s/vlessconfig",
"https://t.me/s/vlessh",
"https://t.me/s/vmesc",
"https://t.me/s/vmess_ir",
"https://t.me/s/vmess_iran",
"https://t.me/s/vmess_vless_v2rayng",
"https://t.me/s/vmessiranproxy",
"https://t.me/s/vmesskhodam",
"https://t.me/s/vmesskhodamm",
"https://t.me/s/vmessorg",
"https://t.me/s/vmessprotocol",
"https://t.me/s/vmessraygan",
"https://t.me/s/vmessx",
"https://t.me/s/vmgit",
"https://t.me/s/vp22ray",
"https://t.me/s/vpean",
"https://t.me/s/vplaf",
"https://t.me/s/vplusvpn_free",
"https://t.me/s/vpn4ir_1",
"https://t.me/s/vpn707",
"https://t.me/s/vpn_accounti",
"https://t.me/s/vpn_arta",
"https://t.me/s/vpn_darkk",
"https://t.me/s/vpn_go67",
"https://t.me/s/vpn_kadeh_iran",
"https://t.me/s/vpn_kanfik",
"https://t.me/s/vpn_land_official",
"https://t.me/s/vpn_mafia",
"https://t.me/s/vpn_mikey",
"https://t.me/s/vpn_nafas",
"https://t.me/s/vpn_proxy_channel",
"https://t.me/s/vpn_proxy_v2ry",
"https://t.me/s/vpn_room",
"https://t.me/s/vpn_tehran",
"https://t.me/s/vpn_v2rang_box",
"https://t.me/s/vpn_v2rayng_gap",
"https://t.me/s/vpn_vip_nor",
"https://t.me/s/vpn_whal",
"https://t.me/s/vpn_zvpn",
"https://t.me/s/vpnafra",
"https://t.me/s/vpnaiden",
"https://t.me/s/vpnamohelp",
"https://t.me/s/vpnazadland",
"https://t.me/s/vpnbigbang",
"https://t.me/s/vpnconfignet",
"https://t.me/s/vpncostumer",
"https://t.me/s/vpneti",
"https://t.me/s/vpnfail_v2ray",
"https://t.me/s/vpnforsale1402",
"https://t.me/s/vpnfree6",
"https://t.me/s/vpnfreeaccounts",
"https://t.me/s/vpnfreeo",
"https://t.me/s/vpnhouse_official",
"https://t.me/s/vpnhub69",
"https://t.me/s/vpnhubmarket",
"https://t.me/s/vpnkanfik",
"https://t.me/s/vpnkar",
"https://t.me/s/vpnkaro",
"https://t.me/s/vpnmasi",
"https://t.me/s/vpnmega1",
"https://t.me/s/vpnmk1",
"https://t.me/s/vpnod",
"https://t.me/s/vpnowl",
"https://t.me/s/vpnplus100",
"https://t.me/s/vpnpopular2023",
"https://t.me/s/vpnservergprc",
"https://t.me/s/vpnskyy",
"https://t.me/s/vpnstorefast",
"https://t.me/s/vpnsupportfast",
"https://t.me/s/vpntako",
"https://t.me/s/vpntwitt",
"https://t.me/s/vpnv2rayngv",
"https://t.me/s/vpnv2rayonline",
"https://t.me/s/vpnv2raytop",
"https://t.me/s/vpnvg",
"https://t.me/s/vpnwedbaz",
"https://t.me/s/vpnwlf",
"https://t.me/s/vpnxyam_ir",
"https://t.me/s/vpnzamin",
"https://t.me/s/vpray3",
"https://t.me/s/vtolink",
"https://t.me/s/vtworay_wolf",
"https://t.me/s/webhube",
"https://t.me/s/webonim",
"https://t.me/s/webovpn",
"https://t.me/s/webshecan",
"https://t.me/s/wirepro_vpn",
"https://t.me/s/wmessorg",
"https://t.me/s/womanlifefreedomvpn",
"https://t.me/s/world_vmess",
"https://t.me/s/wsbvpn",
"https://t.me/s/x2ray_team",
"https://t.me/s/x4azadi",
"https://t.me/s/xbest_speed",
"https://t.me/s/xfavpn",
"https://t.me/s/xiv2ray",
"https://t.me/s/xnxv2ray",
"https://t.me/s/xpnteam",
"https://t.me/s/xuvixc",
"https://t.me/s/xv2ray",
"https://t.me/s/xvproxy",
"https://t.me/s/yarito_media",
"https://t.me/s/yasv2ray",
"https://t.me/s/yekoyekvpn",
"https://t.me/s/zar_vpn",
"https://t.me/s/zarinargo",
"https://t.me/s/zed_vpn",
"https://t.me/s/zede_filteri",
"https://t.me/s/zedmodeonvpn",
"https://t.me/s/zeptovpn",
"https://t.me/s/zilatvpn",
"https://t.me/s/zohalserver"
]

def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


html_pages = []

for url in webpage_addresses:
    response = requests.get(url)
    html_pages.append(response.text)

codes = []

for page in html_pages:
    soup = BeautifulSoup(page, 'html.parser')
    code_tags = soup.find_all('code')

    for code_tag in code_tags:
        code_content = code_tag.text.strip()
        if "vless://" in code_content or "ss://" in code_content or "vmess://" in code_content or "trojan://" in code_content or "tuic://" in code_content or "hysteria://" in code_content or "hy2://" in code_content or "hysteria2://" in code_content or "juicity://" in code_content or "nekoray://" in code_content or "socks4://" in code_content or "socks5://" in code_content or "socks://" in code_content or "naive+" in code_content:
           codes.append(code_content)

codes = list(set(codes))  # Remove duplicates

processed_codes = []

# Get the current date and time
current_date_time = jdatetime.datetime.now(pytz.timezone('Asia/Tehran'))
# Print the current month in letters
current_month = current_date_time.strftime("%b")

# Get the current day as a string
current_day = current_date_time.strftime("%d")

# Increase the current hour by 4 hours
#new_date_time = current_date_time + timedelta(hours=4)

# Get the updated hour as a string
updated_hour = current_date_time.strftime("%H")

updated_minute = current_date_time.strftime("%M")

# Combine the strings to form the final result
final_string = f"{current_month}-{current_day} | {updated_hour}:{updated_minute}"
final_others_string = f"{current_month}-{current_day}"
config_string = "#✅ " + str(final_string) + "-"

for code in codes:
    vmess_parts = code.split("vmess://")
    vless_parts = code.split("vless://")

    for part in vmess_parts + vless_parts:
        if "ss://" in part or "vmess://" in part or "vless://" in part or "trojan://" in part:
            service_name = part.split("serviceName=")[-1].split("&")[0]
            processed_part = part.split("#")[0]
            processed_codes.append(processed_part)

processed_codes = remove_duplicates(processed_codes)

new_processed_codes = []

for code in processed_codes:
    vmess_parts = code.split("vmess://")
    vless_parts = code.split("vless://")

    for part in vmess_parts + vless_parts:
        if "ss://" in part or "vmess://" in part or "vless://" in part or "trojan://" in part:
            service_name = part.split("serviceName=")[-1].split("&")[0]
            processed_part = part.split("#")[0]
            new_processed_codes.append(processed_part)

i = 0
with open("config.txt", "w", encoding="utf-8") as file:
    for code in new_processed_codes:
        if i == 0:
            config_string = "#🌐 به روزرسانی شده در" + final_string + " | هر 15 دقیقه کانفیگ جدید داریم"
        else:
            config_string = "#🌐سرور " + str(i) + " | " + str(final_others_string) + "| MTSRVRS"
        config_final = code + config_string
        file.write(config_final + "\n")
        i += 1
