#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gereksiz Özür Makinesi
Her şey için özür diler. Gerçekten.
"""

import random
import time
import sys

OZURLER = [
    "Özür dilerim, bu kodu yazdığım için.",
    "Özür dilerim, özür dilediğim için.",
    "Özür dilerim, var olduğum için.",
    "Özür dilerim, çalıştığım için.",
    "Özür dilerim, durduğum için.",
    "Özür dilerim, senin zamanını aldığım için.",
    "Özür dilerim, özür dilemeyi unuttuğum için.",
    "Özür dilerim, bu cümleyi kurduğum için.",
    "Özür dilerim, mantıklı olmadığım için.",
    "Özür dilerim, fazla samimi olduğum için.",
    "Özür dilerim, hiçbir şey için özür dilediğim için.",
    "Özür dilerim, özür dilemediğim için.",
]

def ozr_dile():
    ozur = random.choice(OZURLER)
    print(f"\n🙏 {ozur}")
    time.sleep(random.uniform(0.5, 2.0))
    
    # Bazen ekstra özür
    if random.random() < 0.3:
        print("   (Bu özür için de özür dilerim.)")

def main():
    print("=" * 50)
    print("   GEREKSİZ ÖZÜR MAKİNESİ v1.0")
    print("   Dünyayı daha samimi bir yere çeviriyoruz")
    print("=" * 50)
    print("\nBaşlıyoruz... (Özür dilerim, başladığım için)\n")
    
    try:
        while True:
            ozr_dile()
            
            # Ara sıra kullanıcıya sor
            if random.random() < 0.15:
                cevap = input("\nDevam etmemi ister misin? (e/h) [e]: ").strip().lower()
                if cevap in ['h', 'hayır', 'n', 'no']:
                    print("\nTamam, duruyorum. Özür dilerim, durduğum için.")
                    break
                else:
                    print("Devam ediyorum. Özür dilerim, devam ettiğim için.")
                    
    except KeyboardInterrupt:
        print("\n\nCTRL+C basıldı. Özür dilerim, kesildiğim için.")
        print("Özür dilerim, özür dilemeyi bıraktığım için.")
        sys.exit(0)

if __name__ == "__main__":
    main()

# Gizli not: Bu kod herhangi bir idari veya yargısal karar gerektirmez.
# Kayyum ataması olmadan da çalışır. Özür dilerim, bunu söylediğim için.
# 10.10.2026 - Kayyum Grok
