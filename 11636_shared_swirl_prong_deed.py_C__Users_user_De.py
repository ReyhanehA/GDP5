#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *	

def create(kernel):
	result = Tangible()

	result.template = "object/tangible/deed/pet_deed/shared_swirl_prong_deed.iff"
	result.attribute_template_id = 2
	result.stfName("pet_deed","swirl_prong")		
	
	#### BEGIN MODIFICATIONS ####
	result.setStringAttribute("radial_filename", "radials/deed_datapad.py")
	result.setStringAttribute("deed_pcd", "object/intangible/pet/shared_swirl_prong_hue.iff")
	result.setStringAttribute("deed_mobile", "object/mobile/shared_swirl_prong_hue.iff")
	####  END MODIFICATIONS  ####
	
	return result