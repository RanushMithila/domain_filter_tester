import aiohttp
import asyncio
import pandas as pd

domains = open('domains.txt').read().splitlines()

async def check_domain(session, domain):
    results = []
    # Check if domain already includes protocol
    if domain.startswith('http://') or domain.startswith('https://'):
        protocol = domain.split('://')[0]
        try:
            async with session.get(domain, timeout=5) as response:
                results.append({protocol.upper(), response.status})
        except Exception as e:
            results.append(f"{protocol.upper()} not reachable. Error: {e}")
    else:
        for protocol in ["http", "https"]:
            try:
                async with session.get(f'{protocol}://{domain}', timeout=5) as response:
                    results.append({protocol.upper(), response.status})
            except Exception as e:
                results.append(f"{protocol.upper()} not reachable. Error: {e}")
    return {'domain': domain, 'result': results}

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [check_domain(session, domain) for domain in domains]
        results = await asyncio.gather(*tasks)
        df = pd.DataFrame(results)
        df.to_csv('domain_check_results.csv', index=False)

if __name__ == "__main__":
    asyncio.run(main())