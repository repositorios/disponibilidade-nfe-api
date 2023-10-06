# API de disponibilidade NF-e
> Monitora a emissão de Nota Fiscal Eletrônica

APi criada para monitorar o status da emissão de NF-e, foi planejada para fornecer uma interface limpa para uma extensão do Google Chrome.

Pode realizar o download da extensão do Google Chrome [neste link][1].

## Uso

Após baixar o repositório basta executar o `install.sh` com o seguinte comando:

    sudo sh install.sh

Em seguida basta editar seu `crontab` com o comando abaixo:

    crontab -e

E adicionar a linha abaixo:

    * * * * * /usr/bin/python3 /var/www/html/cron.py

## Contribuindo

1. Faça um fork!
2. Crie sua melhoria em um branch: `git checkout -b my-new-feature`
3. Commit suas mudanças: `git commit -am 'Adicionando nova funcionalidade'`
4. Envie ao branch: `git push origin my-new-feature`
5. Envie um pull request :D

## Changelog

#### Versão 1.0.0 *(2023-03-30)*

- Versão inicial.

## Créditos

Renato Tavares ([Github][2], [Twitter][3])

## Licença

[AGPL-3.0 License][4]

[1]:https://chrome.google.com/webstore/detail/consultar-disponibilidade/giikpeklljpljjdhhgnnlgdefikneiih "Download do extensão"
[2]: https://github.com/rat "Github"
[3]: https://twitter.com/renatotavares "Twitter"
[4]: LICENSE "AGPL-3.0"
