# Hybrid Connectivity Hub - Kiełczów Station 

 Project Overview
This project focuses on building an autonomous, off-grid communication node and Command Center. It integrates satellite downlink capabilities (TinyGS) with long-range terrestrial radio mesh networks (Meshtastic). The system leverages Edge Computing principles using recovered hardware and open-source software stack.

Hardware Stack
* **Controller:** Lenovo Miix 300 (Intel Atom Z3735F, 2GB RAM)
* **OS:** Lubuntu 24.04 LTS (Optimized for Headless Operation)
* **Radio Modules:** 2x Heltec Automation V4 (868 MHz LoRa)
* **GNSS:** Quectel L76K (GPS/GLONASS/Galileo support)
* **Power:** Solar-ready (Transitioning to independent power supply)

Technical Features
* **Hybrid Gateway:** Acts as a bridge between LoRa mesh networks and the cloud.
* **Satellite Downlink:** Real-time satellite packet interception via TinyGS network.
* **Professional Edge Management:** Fully managed via SSH over local network.
* **Automated Data Pipelines:** Radio packets and system telemetry are logged directly to GitHub for persistent storage and analysis.

 Current Project Status
- [x] Lubuntu OS installation and Linux environment hardening.
- [x] Secure SSH access and GitHub ED25519 tunnel establishment.
- [ ] Integration of dual Heltec V4 modules via USB serial interface.
- [ ] Deployment of IP66-rated outdoor enclosure and external antenna array.
- [ ] Solar power unit implementation and battery management testing.

---
*Developed & Maintained by Robert Lukowski*
