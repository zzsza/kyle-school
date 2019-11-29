```
#!/bin/bash

## Install Homebrew & Cask
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew tap homebrew/cask-versions

## Update Homebrew
brew update

## Install Python3
brew install python3


## Install Mac Command Line Tools
xcode-select --install

## Install Browsers (Google Chrome, Firefox)
brew cask install google-chrome
brew cask install firefox

## Install HashiCorp Tools 
# brew install terraform

## Install Virtualization Tools (Docker)
brew cask install docker


## Install IDEs (Intellij, Pycharm, Visual Studio Code)
brew cask install visual-studio-code
brew cask install intellij-idea
brew cask install pycharm-ce

# Install important Visual Studio Code Extensions
cat vscode-extensions.txt | xargs -L1 code --install-extension

## Install AWS Tools (AWS CLI & SAM CLI)
pip3 --version
curl -O https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py --user
pip3 install awscli --upgrade --user
aws --version
rm get-pip.py

brew tap aws/tap
brew install aws-sam-cli
sam --version

## Install GCP Tools (gcloud)
brew cask install google-cloud-sdk


## Install Developer utilities (Spectacle, Tree, httpie)
brew cask install spectacle
brew install tree
brew install httpie


## Install Productivity Tools (Slack)
brew cask install slack

## Global Git Config
git config --global push.default current
git config --global core.excludesfile ~/.gitignore
git config --global user.name "<username>"
git config --global user.email <email>
git config --global color.branch auto
git config --global color.diff auto
git config --global color.interactive auto
git config --global color.status auto
git config --global alias.st status
git config --global alias.ci commit
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.lg "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --date=relative"



## Source zshrc
source ~/.zshrc
```
