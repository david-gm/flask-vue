# Flask commands

## run server:

```shell script
# tells app root directory
export FLASK_APP=flask-vue
# tells app environment mode
export FLASK_ENV=development
# runs flask server
flask run
```

## install yarn
```shell script
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
sudo apt update && sudo apt install yarn
```

## install vue
```
# create an assets folder in root directory
mkdir assets
cd assets
# creat yarn module
yarn
# install vue cli dependency
sudo yarn global add @vue/cli
```
if error *execa@3.4.0: The engine "node" is incompatible with this module. Expected version "^8.12.0 || >=9.7.0". Got "8.10.0"*
appears, try the following
```
sudo apt remove npm node
# Using Ubuntu
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
sudo apt-get install -y nodejs
```

## create vue project
```shell script
vue create <project name>
```