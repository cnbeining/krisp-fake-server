# krisp-fake-server

Server for Krisp.AI application. Tested on macOS.

(Badly) Written in Flask.

## Server Setup

1. Setup environment: bare metal, virtualenv, Docker, virtual hosting - however you like.
2. Install dependencies: `pip install -r requirements.txt`
3. Create your private CA and generate SSL cert for `api.krisp.ai`: Azure has a [good guide](https://learn.microsoft.com/en-us/azure/application-gateway/self-signed-certificates).
4. Get your web server working with generated SSL certificate.

## Client Setup

1. Install and trust the private CA you generated.
2. Setup DNS and `hosts` file so `api.krisp.ai` shall be resolved towards your web server. Krisp.app tends to ignore `hosts` file from time to time: a private DNS with verbose log like [NextDNS](https://my.nextdns.io/) or self-hosted [Pi-Hole](https://docs.pi-hole.net/main/basic-install/) or [AdGuard Home](https://github.com/AdguardTeam/AdGuardHome#getting-started) can help you identify those issues: plus you can override DNS records to ensure all requests always go to your web host.
3. `api.krisp.ai` has HSTS preload so you will need to force your browser to trust your own CA so you can log in. For Chromium-based browsers, go to https://api.krisp.ai/v2/health/ in browser to trigger HSTS warning: type `thisisunsafe` to suppress error(yeah, [no kidding](https://stackoverflow.com/questions/44650854/how-to-disable-chrome-hsts-permanently-for-a-subdomain)).
4. Launch `Krisp.app` and do the login flow.

## Debug


- Check whether the application has somehow did not reach your web server. Maybe DNS figured another way out? Double check your DNS settings, and, if you are using Profile for DoH/DoT, ensure the profile is active.
- Maybe the server errored out? Read logs for more info.

## TODO

- [ ] Forward more headers to server
- [ ] Proxy pool
- [ ] Caching
