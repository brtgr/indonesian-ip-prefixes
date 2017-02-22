Generate Indonesian Prefixes
----------------------------

# Background

Repository ini digunakan untuk mendeteksi route dan prefix dari/ke Indonesia. Metode yang digunakan sangat sederhana, kami mengambil prefix Indonesia yang diadvertise ke [OpenIXP](www.openixp.net) dan [IIX](iix.net.id). Prefix yang di generate diambil dari route reflector, dan di translasikan menggunakan script python.

ASN OpenIXP: `7717`

ASN IIX: `7597`

## Generate Prefix Advertised to OpenIXP
```
:foreach i in [/ip route find where bgp-as-path ~ "^7717" received-from=DIRECT-OpenIXP ] do={:put [/ip route get $i dst-address ]}
```

## Generate Prefix Advertised to IIX
```
:foreach i in [/ip route find where bgp-as-path ~ "^7597" received-from=DIRECT-IIX ] do={:put [/ip route get $i dst-address ]}

```

# Cara penggunaan

```
[admin@MikroTik] > /tool fetch url="http://sumberterbuka.beritagar.id/id.rsc" mode=http;                                          
      status: finished
  downloaded: 551KiBz pause]
       total: 551KiB
    duration: 1s
```

Kemudian import file `id.rsc`.

```
[admin@MikroTik] > /import id.rsc
```

# Limitasi

Apa yang sudah ter-generate di sini belum tentu berjalan 100% sempurna, karena ini adalah hasil output dari routing table kami (AS133812). Mungkin filter atau policy di router masing-masing berbeda. Tapi ini akan berguna jika Anda tidak punya peer-connection ke OpenIXP ataupun IIX dan ingin memisahkan bandwidth ke arah local exchange lebih besar daripada internet exchange.
