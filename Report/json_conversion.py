import os
import json
from os import listdir, getcwd
from os.path import join

classes = ["adelholzener_alpenquelle_classic_075", "adelholzener_alpenquelle_naturell_075", "adelholzener_classic_bio_apfelschorle_02", "adelholzener_classic_naturell_02", "adelholzener_gourmet_mineralwasser_02", "augustiner_lagerbraeu_hell_05", "augustiner_weissbier_05", "coca_cola_05", "coca_cola_light_05", "suntory_gokuri_lemonade", "tegernseer_hell_03", "corny_nussvoll", "corny_nussvoll_single", "corny_schoko_banane", "corny_schoko_banane_single", "dr_oetker_vitalis_knuspermuesli_klassisch", "koelln_muesli_fruechte", "koelln_muesli_schoko", "caona_cocoa", "cocoba_cocoa", "cafe_wunderbar_espresso", "douwe_egberts_professional_ground_coffee", "gepa_bio_caffe_crema", "gepa_italienischer_bio_espresso", "apple_braeburn_bundle", "apple_golden_delicious", "apple_granny_smith", "apple_red_boskoop", "avocado", "banana_bundle", "banana_single", "clementine", "clementine_single", "grapes_green_sugraone_seedless", "grapes_sweet_celebration_seedless", "kiwi", "orange_single", "oranges", "pear", "pasta_reggia_elicoidali", "pasta_reggia_fusilli", "pasta_reggia_spaghetti", "franken_tafelreiniger", "pelikan_tintenpatrone_canon", "ethiquable_gruener_tee_ceylon", "gepa_bio_und_fair_fencheltee", "gepa_bio_und_fair_kamillentee", "gepa_bio_und_fair_kraeuterteemischung", "gepa_bio_und_fair_pfefferminztee", "gepa_bio_und_fair_rooibostee", "kilimanjaro_tea_earl_grey", "cucumber", "carrot", "corn_salad", "lettuce", "vine_tomatoes", "roma_vine_tomatoes", "rocket", "salad_iceberg", "zucchini"]

label_dir = '/home/nicstar/Documents/aivero/d2s/d2s_annotations_v1.1/ annotations/D2S_validation_wo_occlusion'

#box form[x,y,w,h]
def convert(size,box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = box[0]*dw
    y = box[1]*dh
    w = box[2]*dw
    h = box[3]*dh
    return (x,y,w,h)

def convert_annotation():
    if not os.path.exists(label_dir):
        os.makedirs(label_dir)
    with open('/home/nicstar/Documents/aivero/d2s/d2s_annotations_v1.1/ annotations/D2S_validation_wo_occlusion.json','r') as f:
        data = json.load(f)
    for item in data['images']:
        image_id = item['id']
        file_name = item['file_name']
        width = item['width']
        height = item['height']
        value = filter(lambda item1: item1['image_id'] == image_id,data['annotations'])
        outfile = open('/home/nicstar/Documents/aivero/d2s/d2s_annotations_v1.1/ annotations/D2S_validation_wo_occlusion/%s.txt'%(file_name[:-4]), 'a+')
        for item2 in value:
            category_id = item2['category_id']
            value1 = filter(lambda item3: item3['id'] == category_id,data['categories'])
            name = value1[0]['name']
            class_id = classes.index(name)
            box = item2['bbox']
            bb = convert((width,height),box)
            outfile.write(str(class_id)+" "+" ".join([str(a) for a in bb]) + '\n')
        outfile.close()

if __name__ == '__main__':
    convert_annotation()
