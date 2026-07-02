# 性能与耗电说明

GrandpaNiu 只维护 Fusion 模块，不再保留低功耗或全覆盖的独立 profile。

性能与耗电主要受 MITM hostname 数量、Body Rewrite、响应脚本、大型 JSON 处理、高频 App 请求和远程规则数量影响。

调整应以缩小具体规则、脚本或 MITM 范围为单位，不能通过重新引入多版本模块来规避问题。Spotify、YouTube 和知乎等核心能力不应因性能调整直接删除。
