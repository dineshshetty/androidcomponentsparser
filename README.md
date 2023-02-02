# androidcomponentsparser
Hacky script to parse AndroidManifest.xml file and provide the list of components along with the intent filter and exported state


Usage: _python3 components_parse.py_

python3 components_parse.py
Enter the path to the APK file: target.apk
I: Using Apktool 2.6.0 on target.apk
I: Loading resource table...
I: Decoding AndroidManifest.xml with resources...
I: Loading resource table from file: /Users/dns/Library/apktool/framework/1.apk
I: Regular manifest package...
I: Decoding file-resources...
I: Decoding values */* XMLs...
I: Baksmaling classes.dex...
I: Baksmaling classes2.dex...
I: Baksmaling classes3.dex...
I: Baksmaling classes4.dex...
I: Baksmaling classes5.dex...
I: Baksmaling classes6.dex...
I: Baksmaling classes7.dex...
I: Copying assets and libs...
I: Copying unknown files...
I: Copying original files...
I: Copying META-INF/services directory
Android Package Name: com.dns.insecurepass
╒══════════════════════════════════════════════════════════════════════════╤══════════╤════════════╤═════════════════╕
│ Name                                                                     │ Type     │ Exported   │ Intent-Filter   │
╞══════════════════════════════════════════════════════════════════════════╪══════════╪════════════╪═════════════════╡
│ com.dns.insecurepass.LocationActivity                                    │ activity │            │ No              │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.dns.insecurepass.SplashScreenActivity                                │ activity │            │ Yes             │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.dns.insecurepass.GoPremiumActivity                                   │ activity │            │ No              │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.cooltechworks.creditcarddesign.CardEditActivity                      │ activity │            │ No              │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.dns.insecurepass.AddNewPaymentCardActivity                           │ activity │            │ No              │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.dns.insecurepass.MasterPasswordActivity                              │ activity │ true       │ No              │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.dns.insecurepass.SettingsActivity                                    │ activity │ true       │ No              │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.dns.insecurepass.RestoreOperation                                    │ activity │            │ No              │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.dns.insecurepass.BackupOperation                                     │ activity │            │ No              │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.dns.insecurepass.ForgotPasswordActivity                              │ activity │            │ No              │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.dns.insecurepass.RegistrationActivity                                │ activity │            │ No              │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.dns.insecurepass.LoginActivity                                       │ activity │            │ No              │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.dns.insecurepass.PinLockOptionsActivity                              │ activity │ true       │ No              │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.dns.insecurepass.GeneratePasswordActivity                            │ activity │            │ No              │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.dns.insecurepass.AccountDetailsView                                  │ activity │            │ No              │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.dns.insecurepass.NewPasswordAddActivity                              │ activity │            │ No              │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.dns.insecurepass.MainActivity                                        │ activity │ true       │ No              │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.dns.insecurepass.CustomPinActivity                                   │ activity │            │ No              │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.aditya.filebrowser.FileBrowser                                       │ activity │            │ No              │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.aditya.filebrowser.FileChooser                                       │ activity │            │ No              │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.aditya.filebrowser.FileBrowserWithCustomHandler                      │ activity │            │ No              │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.aditya.filebrowser.utils.Permissions                                 │ activity │            │ No              │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.nbsp.materialfilepicker.ui.FilePickerActivity                        │ activity │            │ No              │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.google.android.gms.ads.AdActivity                                    │ activity │            │ No              │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.google.android.gms.ads.purchase.InAppPurchaseActivity                │ activity │            │ No              │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.google.android.gms.appinvite.PreviewActivity                         │ activity │ true       │ Yes             │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.google.android.gms.auth.api.signin.internal.SignInHubActivity        │ activity │ false      │ No              │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.google.android.gms.common.api.GoogleApiActivity                      │ activity │ false      │ No              │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.google.android.gms.tagmanager.TagManagerPreviewActivity              │ activity │            │ Yes             │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ androidx.core.content.FileProvider                                       │ provider │ false      │ No              │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.google.firebase.provider.FirebaseInitProvider                        │ provider │ false      │ No              │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.dns.insecurepass.passwordBroadcastReceiver                           │ receiver │ true       │ Yes             │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.dns.insecurepass.confirmationSMSBroadcastReceiver                    │ receiver │ true       │ Yes             │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.google.android.gms.cast.framework.media.MediaIntentReceiver          │ receiver │            │ No              │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.google.android.gms.measurement.AppMeasurementReceiver                │ receiver │ false      │ No              │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.google.android.gms.measurement.AppMeasurementInstallReferrerReceiver │ receiver │            │ Yes             │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.google.firebase.iid.FirebaseInstanceIdReceiver                       │ receiver │ true       │ Yes             │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.google.firebase.iid.FirebaseInstanceIdInternalReceiver               │ receiver │ false      │ No              │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.dns.insecurepass.AdService                                           │ service  │ true       │ No              │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.dns.insecurepass.RemoteLocatorService                                │ service  │ true       │ No              │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.google.android.gms.auth.api.signin.RevocationBoundService            │ service  │ true       │ No              │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.google.android.gms.cast.framework.media.MediaNotificationService     │ service  │            │ No              │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.google.android.gms.cast.framework.ReconnectionService                │ service  │            │ No              │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.google.firebase.messaging.FirebaseMessagingService                   │ service  │ true       │ Yes             │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.google.android.gms.tagmanager.TagManagerService                      │ service  │ false      │ No              │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.google.android.gms.measurement.AppMeasurementService                 │ service  │ false      │ No              │
├──────────────────────────────────────────────────────────────────────────┼──────────┼────────────┼─────────────────┤
│ com.google.firebase.iid.FirebaseInstanceIdService                        │ service  │ true       │ Yes             │
╘══════════════════════════════════════════════════════════════════════════╧══════════╧════════════╧═════════════════╛
