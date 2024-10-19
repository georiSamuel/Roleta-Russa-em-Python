Depois de muitos testes, **nenhum** deles foi eficaz, mesmo com toda as permissões de administrador e mesmo executando na Shell. Pelo que me parece, nenhum programa executável (ou pelo menos programas em Python) que não seja um malware pode deletar ou alterar arquivos ou diretórios do OS. Deve ser uma medida de segurança rígida, ou só a própria linguagem que não tem recursos suficientes  .

Busquei recursos na internet, mas só achei exemplos simples que não funcionavam, o máximo de informação que achei foi num formum, e dizia:

> Just try to remove it manually and still you are getting the permission issues with windows then python script wouldn't work either, you have to get the ownership object from windows. try changing the files permissions then run the python script. Usually windows not allow to delete the files in System32 directory it is a core part of the windows.
>

> Write a proper script and test it with files in user directory first, if it successfully doing your job. then deal with windows for your folders you want to remove.
>  
  

Enfim, talvez não seja mesmo possível realizar essa proeza em Python. Num sistema como Linux, provavalemente funcione, mas no geral, foi um experimento muito interessante.