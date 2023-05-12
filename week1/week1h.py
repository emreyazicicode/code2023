import itertools
text = "ütPKth,xmvQ,ütPK,-X.vDAvDPe,üDEKevyAThqyhM,oPAy,-DəveSqDhM,gDhşDSQPqyh,.D,öyPybyBqyh,KszePk,cQhQ,ütPKexDheh,ayPefe,eEvDP,hySePe,ZX.vQq,Oy.QEmBvQ,qsxebk,ZkOy.QEmBvQ,rtləQPexxDA,uyvÇ,dyPAexynThTh,nDqPe, ylyv, TvTzqyPmBvQhy,aeAybDh,ütPKexDheh,çSDPbyxfyhqyh,xyh,KszD,bevlDxDfDxehe,qsxebk,çSDPbyxfyhqyh,hD,enADxePneheSğ,çSDPbyxfyh,öyPybyBT,şsPe,yvyhqy,əDP,ftP,qDnADxe,.sPqeKk,CeSM,ADDnnt?,KeM,ütPKexD,çSDPbyxfyhT,qDnADKvDqe,qsqeheSk,çSDPbyxfyh,hexD,əDPb,lsxqyhThy,shqeğ,ÖS,AmPpyÇvyPThT,şsPe,yvlyÇ,tzthk,çSDPbyxfyh,iPlDhenAyhTh,AmPpyÇvyPThy,ətfQl,sAlDxeb,KeğM,ı,ütPKexDheh,ayPefe,nexynDA,eqyPDneheh,PDəbDPe, ylyv, TvTzqyPmBvQhy,aeAybDh,qsxebk,Oy.QEmBvQ,Çsxq,sqeb,KeM,bQ,şth,AtPK,qthxynT,ştfvtqtPk,ÖS,levve,ltqy?eD,nenAslvDPeleS,.yPk,-tElDhD,lXəAyf,qsxeveKk,çSDPbyxfyhqyh,hD,enADxePneheSğ,cQ,şth,ütPKexD,bXxtK,AtPK,qthxynThT,bePvDEqePePk,cQ,şth,ütPKexD,ütPK,-X.vDAvDPe,üDEKevyAThTh,yPSQnQhQM,xDhe,AtPK,qthxynThTh,bePvDElDK,yPSQnQhQ,əDxyAy,KszePDh,beP,XvKDqePk"
normal = "Azərbaycan Respublikasının Prezidenti Zati-aliləri cənab İlham Əliyevə.Hörmətli Prezident İlham Əliyev!.Sizin mərhum atanız Prezident Heydər Əliyevin anadan olmasının 100 illiyinin qeyd olunduğu bu günlər görkəmli siyasi xadimin, tarixi şəxsiyyətin və Liderin, müasir müstəqil Azərbaycanın banisinin həyat hekayəsini, nailiyyətlərini xatırlamaq üçün çox yaxşı fürsətdir.Dövlət Təhlükəsizliyi Xidmətində yüksək rütbələrdən başlayaraq keçmiş Sovet İttifaqı rəhbərliyində çox məsul vəzifələrə, müstəqil Azərbaycanı təlatümlərdən xilas edərək inkişaf yoluna çıxarmağa qədər uzanan həyat yolunda o, hər zaman əsl Lider olduğunu sübut etmişdir. Heydər Əliyev güclü məntiqi, zəngin təcrübəsi, qətiyyəti və dərin biliyi ilə müsahiblərini həmişə heyrətləndirirdi. Sizin mərhum atanız dünya liderləri arasında böyük hörmətə malikdir. Mən onu şəxsən tanımaq şərəfinə nail olduğuma görə qürur hissi keçirir və dünya liderlərinin BMT-nin himayəsi altında Nyu-Yorkda Yeni Minilliyi qeyd etmək üçün keçirilən toplantıdakı görüşümüzü dəqiqliklə xatırlayıram. Bu dahi insanla etdiyimiz fikir mübadiləsi mənim üçün çox səmərəli olmaqla bərabər, onun beynəlxalq geosiyasət barədə aydın, düşünülmüş və praktik yönümlü fikirlərindən dərindən təsirlənmişdim.Siz Heydər Əliyevin liderlik irsini Azərbaycan və onun xalqı uğrunda daha böyük yüksəkliklərə qaldırdığınıza görə qürurlanmalısınız. Mən Sizi dost adlandırmaqdan qürur duyur, Sizə və Azərbaycana daha uğurlu gələcək arzu edirəm.Allah Sizi qorusun!Allah Azərbaycanı qorusun!Dərin hörmətlə,zərbaycan Respublikasının Prezidenti Zati-aliləri cənab İlham ƏliyevəHörmətli cənab Prezident!Atanız, Azərbaycan xalqının Ümummilli Lideri Heydər Əliyevin şanlı yubileyini qeyd edərkən, mən də onun nurlu xatirəsini Sizinlə və xalqınızla birgə yad edir və Sizə qoşuluram.Mən bu dahi şəxsiyyətin özünü və onun dinlərarası harmoniya üçün təməl rolunu oynayan dəyərli fikirlərini heç zaman unutmayacağam. Bilirəm ki, Siz Heydər Əliyevin beynəlxalq arenada layiqli yerini tutmuş Azərbaycana inkişaf, tərəqqi və sabitlik gətirən siyasi kursunu uğurla davam etdirdiyiniz üçün onun ruhu şaddır.Ən xoş arzularla,Mayın 10-da Azərbaycanın Misirdəki səfirliyi tərəfindən bu ölkənin Qalyubiyyə vilayətində yerləşən Misir-Azərbaycan dostluq parkında Ulu Öndər Heydər Əliyevin anadan olmasının 100 illiyi ilə əlaqədar tədbir keçirilib.Səfirlikdən AZƏRTAC-a bildiriblər ki, tədbir iştirakçıları əvvəlcə Azərbaycan xalqının Ümummilli Lideri Heydər Əliyevin əziz xatirəsini anaraq, abidəsi önünə əklil qoyub, parkda yerləşən kitabxanada Ulu Öndərə və ölkəmizə həsr edilmiş materiallarla tanış olublar. Səfirlik tərəfindən kitabxanaya kompüter, proyektor və digər texniki avadanlıqlar hədiyyə edilib.Tədbirin açılışında Azərbaycanın və Misirin Dövlət himnləri səsləndirilib.Səfir Elxan Poluxov çıxış edərək Ümummilli Liderin həyat və fəaliyyəti haqqında geniş məlumat verib, Ulu Öndərin mənalı ömür yolundan, dövlətçiliyimiz uğrunda mübarizəsindən söz açıb, onun Azərbaycan xalqının yaddaşında qurucu və xilaskar dövlət xadimi, milli Lider və xalq məhəbbətini qazanan rəhbər kimi əbədilik qazandığını söyləyib. Azərbaycanın Misirlə əlaqələrinin inkişafında Heydər Əliyevin rolu, bu istiqamətdə atdığı addımlar sırasında onun 1994-cü ildə ilk Afrika qitəsinə səfərinin Misirə olduğunu deyən E.Poluxov ölkələrimiz arasında əməkdaşlığın yüksək səviyyədə olduğunu deyib, Ulu Öndərin uzaqgörənliyinin iki xalqın birgə addımlar atmağa imkan verdiyini bildirib.Qalyubiyyə vilayətinin qubernatoru Əbdülhəmid Əl-Hican Heydər Əliyev kimi dahi şəxsiyyətin abidəsini vilayətdə qoyulmasını qürur hissi ilə xatırladaraq, bunun yerli sakinlər üçün şərəf olduğunu vurğulayıb.Misir Nümayəndələr Palatasının üzvü, Misir-Azərbaycan dostluq qrupunun rəhbəri şeyx Əli Cuma çıxışında Azərbaycan Ümummilli lideri Heydər Əliyevin Misirdə həmişə xoş xatirələrə yad edildiyini diqqətə çatdırıb, dünya siyasətində, həmçinin Islam aləmində Heydər Əliyevin xüsusi yeri olduğunu deyib.Senatda Misir-Azərbaycan dostluq qrupunun başçısı Hani Salah Sirriddin Misir-Azərbaycan münasibətlərinin inkişafında Heydər Əliyevin rolundan söhbət açıb, ikitərəfli əlaqələrin bütün səviyyələrdə möhkəmləndirilməsində parlament əməkdaşlığının əhəmiyyətini vurğulayıb, dostluq qruplarının rolunun canlandırılmasını və son zamanlar həyata keçirilən rəsmi səfərləri yüksək qiymətləndirib.Azərbaycanın Misirdəki icmasının rəhbəri S.Nəsibov dahi lider Heydər Əliyevin Azərbaycanı daim inamla irəliyə aparmağa nail olduğunu deyərək, xalqımız üçün ən həlledici anlarda Heydər Əliyevin liderlik keyfiyyətlərinin və uzaqgörənliyinin dövlətçiliyimizi qorumağa, xalqımızı böyük bəlalardan xilas etməyə imkan verdiyini vurğulayıb.Sonda parkda yerləşən kitabxananın yeniyetmələri mədəni və musiqi proqramı ilə çıxış ediblər.Tədbir bir çox yerli mətbuat orqanları tərəfindən geniş işıqlandırılıb."

def text2Freq( text ):
    freqs = {}
    for t in text:
        if t not in freqs:
            freqs[t] = 1.0 / float(len(text))
        else:
            freqs[t] += 1 / float(len(text))
    return freqs

def sortByValue( incoming ):
    return dict(sorted(incoming.items(), key=lambda item: item[1], reverse=True))


sorted_pass = sortByValue(text2Freq(text))
sorted_norm = sortByValue(text2Freq(normal))

sorted_pass_keys = list(sorted_pass.keys())
sorted_norm_keys = list(sorted_norm.keys())




"""
def decorateText( mapper: dict ):
    output = ""
    for t in text:
        output = output + mapper[t]
    print(output)
    return output

mapper = {}
combinator = {}
for i in range(len(sorted_pass)):
    mapper[ sorted_pass_keys[i] ] = sorted_norm_keys[i]
    combinator[ sorted_pass_keys[i] ] = [ sorted_norm_keys[i] ]
    if i > 0:
        combinator[ sorted_pass_keys[i] ].append( sorted_norm_keys[i-1] )
    if i < len(sorted_pass):
        combinator[ sorted_pass_keys[i] ].append( sorted_norm_keys[i+1] )

print(combinator)
keys, values = zip(*combinator.items())
# permutations_dicts = [dict(zip(keys, v)) for v in itertools.product(*values)]
permutations_dicts = [decorateText(dict(zip(keys, v))) for v in itertools.product(*values)]

#for p in permutations_dicts:
#    print( decorateText( p ) )

"""