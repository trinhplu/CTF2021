from Crypto.Util.number import inverse
p = 147763690849150867668225909469550433915451732812463057700984569348470253956194816406951574728889706783894785686020012100588052689320692584241194441102306664861087263417689874062764278453049583722940577602045732615047554285117930803297120866855129431558042684619199933145634615860792724440681809733506643143827
q = 175323579375439355271067762791797570532327618905238153569106939865810515426195444129569514172323381418275130113304584918382539461249836590401476762173083711488347557377316041604414956494612922763528717954203932654977534635925919801687408066965455169210358420975001566564559944039223342904162696905475355996899
ct = 596292271231612321131686159122473317711073015615915915064253118413220412822615362241190111521611313050246341514512111961953491204237421521971882361991462512481672242282334717214714011720623718196102361903922541412181041138425301432671130231232111227311881902552231684311117190121111372302262121892301191042421919215511923157207731921777618016120104244197207218112089979516853621781313521322520134135203255201230611091411123454316418617412416716812920329620887771326912713766143778418205145782436418025401681732351932287819514594242054901751431368017912019322618321218315812421281951841731221831928162726523713916696109173922311513924212812895152924311865209144791116
e = 65537
n = q*p
phi = (p - 1)*( q - 1)
d = inverse(e, phi)
pt = pow(ct, d, n)
print (pt)
