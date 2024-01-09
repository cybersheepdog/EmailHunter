# EmailHunter

[![Build Status](https://img.shields.io/badge/platform-Linux-blue.svg)](https://shields.io/)
![Maintenance](https://img.shields.io/maintenance/yes/2024.svg?style=flat-square)
[![GitHub last commit](https://img.shields.io/github/last-commit/cybersheepdog/EmailHunter.svg?style=flat-square)](https://github.com/cybersheepdog/EmailHunter/commit/master)
![GitHub](https://img.shields.io/github/license/cybersheepdog/EmailHunter)

***Work in Progress***
Will take a list of emails denoted in the config.ini file, log into them and then search for emails with attachments.  It will download the attachments and gather some information about the email such as:
- [ ] Date
- [ ] Sender
- [ ] Subject
- [ ] Return-Path
- [ ] Received

The intent is for this to be able to be used as a collection source for Threat Intelligence.

Other planned features are:
- [ ] Place each attachment into the [Viper2 Framework](https://github.com/viper-framework/viper2)
- [ ] Place other info in a Threat Intelligence Platform such as [OpenCTI](https://github.com/OpenCTI-Platform/opencti)

I will be writting about this in my [blog](https://cybersheepdog.wordpress.com/) and how to set up the various components and what is needed to interact with them.

Thank you for your patience.
