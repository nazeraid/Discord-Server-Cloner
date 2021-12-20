importer le système d'  exploitation
importer la  discorde
de la  discorde . commandes d' importation ext  
importer  asyncio 
importer la  journalisation
importer au  hasard 
de  colorama  import  init
de  colorama  import  Fore , Style
 demandes d' importation
importer  json
importer la  date et l'heure
importer au  hasard
importer le  filetage
importer au  hasard
 heure d' importation
importer le  filetage

initialisation ()
os . système ( "cls"  ou  "clear" )

token  =  input ( '{} \n [>] {} TOKEN: {}' . format ( Fore . RESET , Fore . LIGHTYELLOW_EX , Fore . RESET ))
prefix  =  input ( '{} \n [>] {} PREFIX: {}' . format ( Fore . RESET , Fore . LIGHTYELLOW_EX , Fore . RESET ))
client  =  commandes . Bot ( command_prefix = prefix , case_insensitive = True ,
                      self_bot = Vrai )

cliente . remove_command ( 'aide' )
header  = { "Autorisation" : f'Bot { jeton } ' }
os . system ( 'cls'  if  os . name  ==  'nt'  else  'clear' )
os . system ( 'cls'  if  os . name  ==  'nt'  else  'clear' )

intentions  =  discorde . Intentions . tout ()
intentions . membres  =  Vrai

@ Client . un événement
async  def  on_ready ():
    imprimer ( '------' )
    print ( '{} \n [>] {} Selfbot en cours d'exécution... {}' . format ( Fore . RESET , Fore . LIGHTYELLOW_EX , Fore . RESET ))
    print ( '{} \n [>] {} Commande :{} {}copyserver \n ' . format ( Fore . RESET , Fore . LIGHTYELLOW_EX , Fore . RESET , prefix ))
    print ( ' - Connecté en tant que '  +  client . utilisateur . nom )
    print ( ' - ID utilisateur : '  +  str ( client . utilisateur . id ))
    print ( ' \n ------ \n ' )


@ Client . commande ()
 serveur de copie async def  ( ctx ):
    attendre  ctx . message . supprimer ()
    wow  =  attendre le  client . create_guild ( f'backup- { ctx . guild . nom } ' )
    attend  asyncio . dormir ( 4 )
    pour  g  dans  client . guildes :
        if  f'backup- { ctx . guilde . nom } '  dans  g . nom :
            pour  c  dans  g . canaux :
                attendre  c . supprimer ()
            pour  cate  dans  ctx . guilde . catégories :
                x  =  attendre  g . create_category ( f" { cate . name } " )
                pour  chann  dans  cate . canaux :
                    si  isinstance ( chann , discorde . VoiceChannel ):
                        attendre  x . create_voice_channel ( f" { cann } " )
                    si  isinstance ( chann , discorde . TextChannel ):
                        attendre  x . create_text_channel ( f" { cann } " )
            print ( ctx . guilde . rôles )
    pour le  rôle  dans  ctx . guilde . rôles [:: - 1 ] :
        si  rôle . nom  !=  "@tout le monde" :
            essaie :
                attend  wow . create_role ( nom = rôle . nom , couleur = rôle . couleur , permissions = rôle . autorisations , Palan = rôle . treuil , mentionable = rôle . mentionable )
                print ( f"Créé un nouveau rôle : { role . name } " )
            sauf :
                Pause

cliente . run ( token , bot = False )
