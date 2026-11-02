# NielloPlayer 隐私政策

**生效日期：2026 年 11 月 1 日　　最后更新：2026 年 11 月 1 日**

当你使用 NielloPlayer 时，你是在信任我们处理与你有关的信息。我们清楚这份责任的分量，会尽力保护这些信息，并让你始终掌握对它们的控制权。

本隐私政策旨在帮助你了解我们处理哪些信息、为什么处理，以及你可以如何查看、管理和删除这些信息。

你可以通过下列标题了解我们在隐私保护方面的做法。如有任何疑问，请通过文末的方式联系我们。

---

## 目录

- [我们是谁](#我们是谁)
- [本政策涵盖什么](#本政策涵盖什么)
- [我们不索取的信息](#我们不索取的信息)
- [应用在你的设备上处理的信息](#应用在你的设备上处理的信息)
- [应用使用的权限](#应用使用的权限)
- [可选打赏](#可选打赏)
- [诊断信息](#诊断信息)
- [信息的共享](#信息的共享)
- [信息的安全](#信息的安全)
- [保留与删除](#保留与删除)
- [你的权利](#你的权利)
- [处理的法律依据](#处理的法律依据)
- [儿童和个人数据](#儿童和个人数据)
- [不出售、不共享](#不出售不共享)
- [政策变更](#政策变更)
- [与我们联系](#与我们联系)

## 我们是谁

NielloPlayer（下称「本应用」）是一款 Android 平台的离线音乐播放器，由 NielloPlayer 的独立开发者提供。

本政策所述处理的控制者是我们。你可以通过 Google Play 商品页「开发者联系信息」中公布的邮箱与我们联系；涉及本政策或你的信息的任何请求，都可以发往该邮箱。

## 本政策涵盖什么

本政策说明应用在你的设备上处理哪些信息、出于什么目的，以及你对此拥有哪些选择。它适用于 Android 版本。

本政策只在线上提供，应用内不保存副本：你在应用里点开的就是当前这一版，不会读到随安装包一起变旧的版本。

它不涵盖你把文件交给其它应用之后发生的事情。从那一刻起，适用的是接收方应用自己的政策，详见「信息的共享」。

## 我们不索取的信息

本应用不设账号，无需注册或登录。我们不索取你的姓名、邮箱地址、电话号码或通讯地址，也不收集你的联系人、短信与通话记录、照片与视频、日历、位置或广告标识符。

应用内没有广告，没有接入分析、社交登录或行为追踪类的第三方 SDK。我们不做用户画像，不依据你的使用行为做定向推荐，也不进行任何自动化决策。

## 应用在你的设备上处理的信息

**曲库与播放状态。** 为了播放音乐，应用会读取你设备上存储的音频文件。曲库索引、播放队列、播放位置、音质与均衡器设置，以及歌曲与歌词的对应关系，保存在应用私有目录中，以便下次打开时恢复你此前的状态。这些信息留在你的设备上，不会发送给我们。

**你选择的文件夹。** 系统媒体库之外的文件夹，例如 SD 卡上的音乐文件夹，只能通过 Android 系统文件选择器访问。应用只能读取你亲自选中的那个文件夹，读不到其它位置，也不申请全盘文件访问权限。你自行添加的歌词文件同样经由这个选择器授权。

**接收目录。** 通过蓝牙、局域网或网页收到的文件，写入你在「设置 → 曲库 → 接收文件夹」中指定的目录，默认是设备公共存储中的 `Music/NielloPlayer`。该目录的内容由你自行管理，详见「信息的共享」。

## 应用使用的权限

每一项权限都只在对应功能被使用时才起作用，我们不会在你还未用到该功能时提前索要，也不会因为你拒绝某项可选权限而限制基础播放功能。

**音频文件。** Android 13 及以上使用 `READ_MEDIA_AUDIO`，Android 10 至 12 使用 `READ_EXTERNAL_STORAGE`，用于扫描并播放你的音乐。`WRITE_EXTERNAL_STORAGE` 仅对 Android 10 及以下声明，用于保留你选定的文件夹。你可以在系统设置中随时收回这些权限，收回后应用只显示已经索引过的内容。

**网络。** `INTERNET` 用于四件事：在本机提供一个局域网网页（网页传歌）、在同一局域网内发现对端设备、在你选择打赏时与 Google Play 通信、以及加载本政策的在线页面。应用不运营任何自有服务器，也不上传你的曲库、歌词或设置。

**Wi-Fi 与热点状态。** `ACCESS_WIFI_STATE` 与 `CHANGE_WIFI_STATE` 用于读取 Wi-Fi 是否已连接、热点是否已开启，以便告诉你该访问哪个地址、该给什么提示。部分 Android 版本上，系统要求 `CHANGE_WIFI_STATE` 才能查询热点状态，这只是读取的前提。应用从不打开或关闭 Wi-Fi 与热点，只复用你自己在系统设置里开启的那个，也不具备把蜂窝数据共享给其它设备的能力。

**蓝牙。** `BLUETOOTH_CONNECT` 用于耳机播放（A2DP）与列出已配对设备。`BLUETOOTH_SCAN` 已向系统声明不用于推断位置（`neverForLocation`），用于在应用内发现附近的传送目标。`BLUETOOTH_ADVERTISE` 用于在你打开接收页期间，让对端设备能够发现本机——该状态最长持续 300 秒，到期后由系统自动恢复为不可被发现，应用无法延长。Android 11 及以下没有上述三项细分权限，对应的能力由安装时授予的 `BLUETOOTH` 与 `BLUETOOTH_ADMIN` 覆盖，应用仅用于蓝牙耳机播放与传歌。

Android 11 及以下，系统把蓝牙扫描与位置权限绑定在一起。应用仅对这些版本声明 `ACCESS_FINE_LOCATION`，且只在你打开蓝牙发现或接收页时于应用内询问一次。你可以拒绝，拒绝后仍能向已配对的设备发送。应用从不读取、不存储、不上传任何位置值。

**前台服务与通知。** `FOREGROUND_SERVICE` 与 `FOREGROUND_SERVICE_MEDIA_PLAYBACK` 用于让音乐在后台继续播放；`POST_NOTIFICATIONS` 用于在锁屏与通知栏显示播放控制。

**结算。** `com.android.vending.BILLING` 是 Google Play 提供可选打赏所必需的权限。

## 可选打赏

打赏完全出于自愿，并完全由 Google Play 结算处理。

Google 作为独立的控制者，按其自身的隐私政策（[policies.google.com/privacy](https://policies.google.com/privacy)）接收并处理你的支付信息。我们在任何环节都不接收、不查看、不存储你的卡号、账单地址或 Google 账户，购买记录也不会进入本应用。

与打赏有关的唯一本地记录，是一个「有一笔打赏还没当面道谢」的标记，用于你下次打开打赏页时显示对应的感谢语。它不含金额，也不含任何支付凭据，卸载应用即被删除。

打赏不解锁任何功能。不付费也能使用全部功能。

## 诊断信息

由于应用通过 Google Play 分发，Google 会在系统层面收集应用的质量数据，也就是 Android vitals：崩溃次数与堆栈、无响应（ANR）事件、启动耗时、耗电与内存占用、权限授予与拒绝的情况，以及发生这些问题时的应用版本、Android 版本、设备型号与国家/地区。这些数据由 Google Play 直接收集，不需要应用内嵌任何代码，也不经过我们。它的用途限于评估与改进应用质量，我们只能通过 Play 管理中心看到聚合后的结果，看不到具体某个用户的记录。

这部分收集由 Google 作为独立的控制者进行，受 Google 自身隐私政策约束。你可以在设备的「设置 → Google → 使用情况和诊断信息」中关闭共享；关闭后 Google 不会再从你这台设备收集这些数据。

## 信息的共享

我们不出售、不出租、不交换你的信息，也不为广告或跨应用追踪而共享。

有两种情形会把文件交给别的应用，且都由你发起：

**蓝牙传歌。** 应用会打开 Android 系统的分享面板，接收方应用由你选择。文件交给对方之后，其保存、复制与再分发由该应用的政策约束，不在本政策范围内。

**接收目录。** 默认的 `Music/NielloPlayer` 位于设备公共存储，系统允许其它应用读取其中的文件。你若把接收目录改到其它位置，可读范围由 Android 的存储规则与你授予的权限决定，这一选择由你作出。

除 Google Play 结算与上文所述的 Android vitals 之外，我们不与任何第三方共享你的信息，也不存在需要向境外传输你曲库信息的情形。你的曲库、歌词、播放记录与设置始终留在你的设备上，从未被传输到任何地方。

## 信息的安全

应用私有目录受 Android 应用沙箱保护，其它应用无法读取。

我们不运营任何接收你数据的后台服务，播放功能不依赖网络，因此你的曲库与设置不可能经由我们的服务器被读取。

在你自己的浏览器中打开的链接所产生的数据，由你的浏览器处理。

本政策的在线页面托管在 GitHub Pages，在应用内以系统浏览器的「自定义标签页」打开：地址栏由浏览器渲染，你可以据此确认自己确实在 `arcanesparkle.github.io` 上，而不是某个应用内的套壳页面。GitHub 作为托管方会收到这次请求的技术信息，例如 IP 地址与请求时间，用于投递页面；浏览器也可能按它自身的设置保留这次访问的记录与缓存，你在页面里选过的显示语言同样存在浏览器自己那边。这些都发生在浏览器与托管方之间：应用不读取页面内容，也无法控制浏览器保留什么。

## 保留与删除

只要你保留本应用，你的信息就留在你的设备上。

卸载应用会删除私有目录中的曲库索引、播放队列与全部设置，我们不保留副本——不存在需要你另行申请删除的云端数据。

应用没有单独的「清除曲库」命令。目前从头重建索引的方式是卸载后重装。

界面显示与后台播放所需的播放状态只存在于内存中，退出应用后释放。

## 你的权利

根据你所在地区的法律，你可能拥有下列权利：访问我们持有的与你有关的信息、要求更正不准确的信息、要求删除、限制或反对处理、以及要求以可携带的形式获取这些信息。

由于你的信息只存在于你的设备上、我们没有任何副本，这些权利可以直接行使：

- **访问与更正**：在应用内查看并修改曲库、目录与全部设置。
- **删除**：卸载应用即删除全部本地数据。
- **撤回同意**：随时在系统设置中撤销任何已授予的权限，撤销后对应功能停止工作，其余功能不受影响。

如果你认为我们的处理违反了数据保护法律，你有权向你的居住地、工作地或涉嫌侵权行为发生地的监管机构提出投诉。你也可以先联系我们，我们会尽力直接解决。

## 处理的法律依据

在适用《通用数据保护条例》（GDPR）的情况下，我们依据以下基础处理信息：

- **履行合同**（第 6(1)(b) 条）：读取你的音频以播放、记住你的播放位置与音质设置、按你指定的目录收取文件。这些处理是提供你请求的服务所必需的。
- **你的同意**（第 6(1)(a) 条）：蓝牙发现等可选权限。你可以随时撤回，撤回不影响此前处理的合法性。

我们不以「合法利益」为依据进行广告、画像或行为分析，因为本应用不做这些事。

## 儿童和个人数据

本应用不面向 13 岁以下儿童，我们也不会有意收集他们的信息。

由于应用向任何人都不收集个人信息，家长无需为孩子使用本应用做任何额外设置。

## 不出售、不共享

按《加州消费者隐私法》及其修正案（CCPA/CPRA）对「出售」与「共享」的定义，我们不出售、也不共享个人信息。本应用没有广告，也没有接入用于广告或画像的分析 SDK；我们不从你的信息中获取任何商业收益。这一情况不随时间变化。

## 政策变更

本政策如有变更，我们会更新本页内容与上方的最后更新日期。

若变更影响信息的处理方式，我们会在生效之前于应用内或商店页面说明，而不是仅更新日期。

## 与我们联系

关于本政策或你的信息，可通过 Google Play 商品页「开发者联系信息」中公布的开发者邮箱与我们联系。

---

**Summary (English)**: This policy explains how NielloPlayer handles your information. NielloPlayer is an offline music player for Android published by its independent developer, who is the controller of the processing described here. The app has no account and does not ask for your name, email address, phone number or postal address. Your library index, playback queue, playback position, audio and equalizer settings and lyrics stay in the app's private storage on your device and are not sent to us. Folders are accessed only through Android's system file picker. Because the app is distributed through Google Play, Google collects app quality data at platform level as Android vitals — crashes and stack traces, ANRs, start-up time, battery and memory use, permission outcomes, plus app version, Android version, device model and country/region. This requires no code in the app, it does not pass through us, and we only see aggregated results in Play Console; you can turn it off in Settings → Google → Usage & diagnostics. This policy is available online only and is not bundled with the app; it is hosted on GitHub Pages and opened inside the app as a browser custom tab, with the address bar rendered by the browser so you can confirm you are on the official domain. GitHub receives the technical information needed to deliver the page, such as your IP address and the time of the request, and the browser may keep its own record or cache of that visit. Optional tips are processed entirely by Google Play Billing, with Google acting as an independent controller under its own privacy policy; we never receive, view or store your payment details, and tipping unlocks no features. We do not sell or share personal information as defined by the CCPA/CPRA. Legal bases under the GDPR are performance of the service you requested (Article 6(1)(b)) and your consent for optional permissions (Article 6(1)(a)), which you can withdraw at any time. Uninstalling the app deletes its index, queue and settings, and we keep no copy.
