package com.isc.dualPrint;
import android.app.Activity;
import android.os.Handler;
import android.app.AlertDialog;
import android.content.DialogInterface;
import android.graphics.Color;
import android.os.Bundle;
import android.widget.Toast;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.ListView;
import android.widget.ArrayAdapter;
import java.util.Hashtable;
import android.widget.AdapterView;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.AdapterView.OnItemClickListener;
import android.widget.EditText;
import android.view.View.OnKeyListener;
import android.view.KeyEvent;
import android.widget.ProgressBar;
import java.util.Random;
import android.widget.TextView;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.ImageView;
import java.util.ArrayList;
import java.util.Arrays;
//EndImports

public class dualPrint extends Activity {
public int iscVcapApple = 5000;
public int iscVn8 = 8;
public int iscVn6 = 6;
public int iscVn4 = 4;
public int iscVn0 = 0;
public int iscVn2m = 2;
public int iscVnm1 = 1;
public String iscVparImpTest = "";
public int iscVcapAndro = 78;
public String iscVlink_pHelp_Loc = "redirect.html";
public int iscVwAbout = 0;
public String iscVlink_license = "http://www.opensource.org/licenses/MIT";
public String iscVlink_web = "http://www.dualPrint.org/";
public String iscVNotifyOSD_Par = "notify-send \'dualPrint: Even Copy\' \'The seccond print set has been copied to the clipboard. You may paste it in the print dialog.\'";
public String iscVNotifyOSD_Imp = "notify-send \'dualPrint: Odd Copy\' \'The first print set has been copied to the clipboard. You may paste it in the print dialog.\'";
public int iscVn2 = 2;
public String iscVcoma = ",";
public String iscVguion = "-";
public int iscVn = 12;
public int iscVsl = 4;
public int iscVstart = 1;
public int iscVcount = 0;
public String iscVnText = "12";
public String iscVslText = "4";
public String iscVstartText = "1";
public String iscVwPar = "";
public String iscVwrite = "write";
public int iscVn1 = 1;
public String iscVcountText = "countText";
public int iscVqTest = 0;
public int iscVqDifference = 0;
public String iscVwImpar = "";
public String iscVlink = "";
public String iscVnullText = "";
public String iscVlink_pHelp_M = "http://www.dualprint.org/";
public String iscVtotal = "Total: ";
public String iscVtotalPages = "";
private TextView iscWindow178nQ0;
private TextView iscWindow178slidesQ0;
private EditText iscWindow178n0;
private EditText iscWindow178sl0;
private Button iscWindow178bStart0;
private TextView iscWindow178inicioQ0;
private EditText iscWindow178start0;
private TextView iscWindow178infoImpar0;
private EditText iscWindow178wImpar0;
private TextView iscWindow178parInfo0;
private EditText iscWindow178wPar0;
private ImageView iscWindow178CI0;
private ImageView iscWindow178CP0;
private Button iscWindow178about0;
private Button iscWindow178paper0;
private ImageView iscWindow178header0;

private ImageView iscWindow177icon0;
private TextView iscWindow177info0;
private TextView iscWindow177rights0;
private Button iscWindow177close0;
private Button iscWindow177web0;
private TextView iscWindow177MIT0;
private TextView iscWindow177version0;
private TextView iscWindow177dualprint0;
private Button iscWindow177license0;
private TextView iscWindow177illumination0;
private TextView iscWindow177info10;
private TextView iscWindow177info20;
private TextView iscWindow177MIT10;

private WebView iscWindow11WebBrowser0;
private Button iscWindow11return0;

//EndOfGlobalVariables


@Override
public void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
iscWindow178();
//iscApp1Launched
}

private class ISCWebViewClient extends WebViewClient {
@Override
public boolean shouldOverrideUrlLoading(WebView view, String url) {
view.loadUrl(url);
return true;
}
}

public void iscHide_Keyboard2()
{
//iscHide_Keyboard2Done}


public void iscTargetIs3()
{
//iscTargetIs3Android
}


public void iscFloat_to_integer5()
{
  //Casting to integer  int integerNum = iscVqDifference;  iscVqDifference = integerNum;//iscFloat_to_integer5Done}


public void iscPortalDestination6()
{
iscSubtract19();
iscDivide17();
iscDivide16();
iscAdd18();
iscTargetIs3();
iscConvertNumberToText14();
//iscPortalDestination6Arrived
}


public void iscConvertNumberToText7()
{
iscVwrite = String.valueOf(iscVcount);
//iscConvertNumberToText7Done
}


public void iscSetCanvasPicture8()
{
iscWindow178header0.setImageResource(R.drawable.header);
//iscSetCanvasPicture8Done
}


public void iscSetCanvasPicture9()
{
iscWindow178CP0.setImageResource(R.drawable.copy);
//iscSetCanvasPicture9Done
}


public void iscSetCanvasPicture10()
{
iscWindow178CI0.setImageResource(R.drawable.copy);
//iscSetCanvasPicture10Done
}


public void iscSetText12()
{
iscVlink = iscVlink_pHelp_M;
iscTargetIs158();
//iscSetText12Done
}


public void iscSetText13()
{
iscVlink = iscVlink_pHelp_Loc;
iscTargetIs158();
//iscSetText13Done
}


public void iscConvertNumberToText14()
{
iscVtotalPages = String.valueOf(iscVqDifference);
iscCombineText15();
//iscConvertNumberToText14Done
}


public void iscCombineText15()
{
iscVtotalPages = iscVtotal + iscVtotalPages;
iscSetButton152();
//iscCombineText15Done
}


public void iscDivide16()
{
iscVqDifference = iscVqDifference / iscVn2;
//iscDivide16Done
}


public void iscDivide17()
{
iscVqDifference = iscVqDifference / iscVsl;
//iscDivide17Done
}


public void iscAdd18()
{
iscVqDifference = iscVqDifference + iscVn1;
//iscAdd18Done
}


public void iscSubtract19()
{
iscVqDifference = iscVn - iscVstart;
//iscSubtract19Done
}


public void iscClipboard_Copy21()
{
//iscClipboard_Copy21Done
}


public void iscRunShellScript23()
{
//iscRunShellScript23Done
}


public void iscIf_Linux25()
{
//iscIf_Linux25Else
}


public void iscPortalDeparture26()
{
iscPortalDestination144();
//iscPortalDeparture26Done
}


public void iscIfThen27()
{
if (iscVqTest > iscVn)
{
iscPortalDeparture26();
//iscIfThen27True

}
else
{
iscPortalDeparture34();
//iscIfThen27False
}
}


public void iscIfThen31()
{
if (iscVqTest == iscVn)
{
iscPortalDeparture32();
iscPortalDeparture150();
//iscIfThen31True

}
else
{
iscDivide33();
iscIfThen36();
iscPortalDeparture150();
//iscIfThen31False
}
}


public void iscPortalDeparture32()
{
iscPortalDestination98();
//iscPortalDeparture32Done
}


public void iscDivide33()
{
iscVqDifference = iscVn / iscVn2;
//iscDivide33Done
}


public void iscPortalDeparture34()
{
iscPortalDestination128();
//iscPortalDeparture34Done
}


public void iscIfThen36()
{
if (iscVqTest < iscVqDifference)
{
iscPortalDeparture34();
//iscIfThen36True

}
else
{
iscIfThen63();
//iscIfThen36False
}
}


public void iscDoWhile38()
{
while (iscVcount < iscVn)
{
iscCombineText132();
iscConvertNumberToText56();
iscCombineText125();
iscAdd136();
iscAdd137();
//iscDoWhile38Loop

}
iscSetText49();
iscConvertTextToNumber146();
iscPortalDeparture150();
//iscDoWhile38Finished
}


public void iscDoWhile39()
{
while (iscVcount < iscVn)
{
iscCombineText132();
iscConvertNumberToText56();
iscCombineText125();
iscAdd136();
iscAdd137();
//iscDoWhile39Loop

}
iscSetText54();
iscAdd136();
iscAdd137();
iscDoWhile38();
//iscDoWhile39Finished
}


public void iscMessageBox40()
{
AlertDialog.Builder alertbox = new AlertDialog.Builder(this);
alertbox.setMessage("The starting page should be lower than the total of pages to print.");
alertbox.setNeutralButton("Ok", new DialogInterface.OnClickListener() {
public void onClick(DialogInterface arg0, int arg1) {
//iscMessageBox40Closed
}
});
alertbox.show();
}


public void iscRunShellScript41()
{
//iscRunShellScript41Done
}


public void iscIf_Linux43()
{
//iscIf_Linux43Else
}


public void iscAdd44()
{
iscVqTest = iscVqTest + iscVsl;
//iscAdd44Done
}


public void iscAdd45()
{
iscVcount = iscVcount + iscVqDifference;
//iscAdd45Done
}


public void iscIfThen46()
{
if (iscVwAbout == iscVn1)
{
iscWindow177();
//iscIfThen46True

}
else
{
iscWindow178();
//iscIfThen46False
}
}


public void iscSetWebBrowser47()
{
iscWindow11WebBrowser0 = (WebView)this.findViewById(R.id.iscWindow11WebBrowser0);
iscWindow11WebBrowser0.setWebViewClient(new ISCWebViewClient());
iscWindow11WebBrowser0.getSettings().setJavaScriptEnabled(true);
iscWindow11WebBrowser0.loadUrl(iscVlink);
//iscSetWebBrowser47Done
}


public void iscMessageBox48()
{
AlertDialog.Builder alertbox = new AlertDialog.Builder(this);
alertbox.setMessage("You should print at least 1 page per side.");
alertbox.setNeutralButton("Ok", new DialogInterface.OnClickListener() {
public void onClick(DialogInterface arg0, int arg1) {
//iscMessageBox48Closed
}
});
alertbox.show();
}


public void iscSetText49()
{
iscVwPar = iscVwrite;
iscSetTextBox78();
iscSetTextBox102();
iscTargetIs155();
//iscSetText49Done
}


public void iscTargetIs50()
{
iscSetText12();
//iscTargetIs50Android
}


public void iscSubtract51()
{
iscVqTest = iscVqTest - iscVn1;
//iscSubtract51Done
}


public void iscSubtract52()
{
iscVqDifference = iscVqTest - iscVn;
iscSubtract53();
//iscSubtract52Done
}


public void iscSubtract53()
{
iscVqDifference = iscVsl - iscVqDifference;
iscAdd45();
//iscSubtract53Done
}


public void iscSetText54()
{
iscVwImpar = iscVwrite;
iscAdd123();
//iscSetText54Done
}


public void iscAdd55()
{
iscVqTest = iscVqTest + iscVn1;
//iscAdd55Done
}


public void iscConvertNumberToText56()
{
iscVcountText = String.valueOf(iscVcount);
//iscConvertNumberToText56Done
}


public void iscIfThen57()
{
if (iscVsl == iscVn1)
{
iscPortalDeparture59();
iscSetCanvasPicture8();
//iscIfThen57True

}
else
{
iscTargetIs159();
//iscIfThen57False
}
}


public void iscPortalDestination58()
{
iscAdd129();
iscSubtract51();
iscIfThen127();
//iscPortalDestination58Arrived
}


public void iscPortalDeparture59()
{
iscPortalDestination139();
//iscPortalDeparture59Done
}


public void iscMessageBox60()
{
AlertDialog.Builder alertbox = new AlertDialog.Builder(this);
alertbox.setMessage("The sum of the starting page and the pages per side should be less than or equal to the total of pages to print.");
alertbox.setNeutralButton("Ok", new DialogInterface.OnClickListener() {
public void onClick(DialogInterface arg0, int arg1) {
//iscMessageBox60Closed
}
});
alertbox.show();
}


public void iscIfThen62()
{
if (iscVqTest > iscVn)
{
iscMessageBox60();
//iscIfThen62True

}
else
{
iscIfThen57();
//iscIfThen62False
}
}


public void iscIfThen63()
{
if (iscVqTest == iscVqDifference)
{
iscPortalDeparture34();
//iscIfThen63True

}
else
{
iscAdd65();
iscAdd44();
iscIfThen27();
//iscIfThen63False
}
}


public void iscMessageBox64()
{
AlertDialog.Builder alertbox = new AlertDialog.Builder(this);
alertbox.setMessage("The number of pages per side should be less than the total of pages to print.");
alertbox.setNeutralButton("Ok", new DialogInterface.OnClickListener() {
public void onClick(DialogInterface arg0, int arg1) {
//iscMessageBox64Closed
}
});
alertbox.show();
}


public void iscAdd65()
{
iscVqTest = iscVstart + iscVsl;
//iscAdd65Done
}


public void iscCombineText67()
{
iscVwrite = iscVwrite + iscVguion;
//iscCombineText67Done
}


public void iscAppQuit69()
{
this.finish();}


public void iscPortalDeparture70()
{
iscPortalDestination72();
//iscPortalDeparture70Done
}


public void iscPortalDeparture71()
{
iscPortalDestination58();
//iscPortalDeparture71Done
}


public void iscPortalDestination72()
{
iscAdd136();
iscAdd137();
iscConvertNumberToText56();
iscCombineText125();
iscPortalDeparture71();
//iscPortalDestination72Arrived
}


public void iscSetTextBox78()
{
iscWindow178wImpar0 = (EditText)this.findViewById(R.id.iscWindow178wImpar0);
iscWindow178wImpar0.setText(iscVwImpar);
//iscSetTextBox78Done
}


public void iscIfThen79()
{
if (iscVqTest == iscVn)
{
iscCombineText67();
iscAdd136();
iscSubtract124();
iscConvertNumberToText56();
iscCombineText125();
//iscIfThen79True

}
else
{
iscCombineText67();
iscSubtract52();
iscSubtract124();
iscConvertNumberToText56();
iscConvertNumberToText56();
iscCombineText125();
//iscIfThen79False
}
}


public void iscIfThen80()
{
if (iscVqTest == iscVn)
{
iscCombineText132();
iscAdd136();
iscAdd137();
iscConvertNumberToText56();
iscCombineText125();
//iscIfThen80True

}
else
{
//iscIfThen80False
}
}


public void iscMessageBox96()
{
AlertDialog.Builder alertbox = new AlertDialog.Builder(this);
alertbox.setMessage("The document must have 2 pages at least.");
alertbox.setNeutralButton("Ok", new DialogInterface.OnClickListener() {
public void onClick(DialogInterface arg0, int arg1) {
//iscMessageBox96Closed
}
});
alertbox.show();
}


public void iscMessageBox97()
{
AlertDialog.Builder alertbox = new AlertDialog.Builder(this);
alertbox.setMessage("Your print should start from page 1 forward.");
alertbox.setNeutralButton("Ok", new DialogInterface.OnClickListener() {
public void onClick(DialogInterface arg0, int arg1) {
//iscMessageBox97Closed
}
});
alertbox.show();
}


public void iscPortalDestination98()
{
iscSetNumber133();
iscCombineText67();
iscPortalDeparture140();
iscSetText54();
iscSetText49();
//iscPortalDestination98Arrived
}


public void iscIfThen99()
{
if (iscVstart < iscVn)
{
iscIfThen103();
//iscIfThen99True

}
else
{
iscMessageBox40();
//iscIfThen99False
}
}


public void iscIfThen100()
{
if (iscVstart < iscVn1)
{
iscMessageBox97();
//iscIfThen100True

}
else
{
iscIfThen115();
//iscIfThen100False
}
}


public void iscSetTextBox102()
{
iscWindow178wPar0 = (EditText)this.findViewById(R.id.iscWindow178wPar0);
iscWindow178wPar0.setText(iscVwPar);
//iscSetTextBox102Done
}


public void iscIfThen103()
{
if (iscVsl < iscVn)
{
iscAdd65();
iscIfThen62();
//iscIfThen103True

}
else
{
iscMessageBox64();
//iscIfThen103False
}
}


public void iscPortalDestination104()
{
iscPortalDeparture140();
iscSetText54();
iscCombineText67();
iscPortalDeparture140();
iscSetText49();
//iscPortalDestination104Arrived
}


public void iscPortalDeparture105()
{
iscPortalDestination104();
//iscPortalDeparture105Done
}


public void iscIfThen114()
{
if (iscVn < iscVn2)
{
iscMessageBox96();
//iscIfThen114True

}
else
{
iscIfThen100();
//iscIfThen114False
}
}


public void iscIfThen115()
{
if (iscVsl < iscVn1)
{
iscMessageBox48();
//iscIfThen115True

}
else
{
iscIfThen99();
//iscIfThen115False
}
}


public void iscGetTextBox116()
{
iscWindow178start0 = (EditText)this.findViewById(R.id.iscWindow178start0);
String strThisString = iscWindow178start0.getText().toString();
iscVstartText = strThisString;
iscGetTextBox117();
//iscGetTextBox116Done
}


public void iscGetTextBox117()
{
iscWindow178sl0 = (EditText)this.findViewById(R.id.iscWindow178sl0);
String strThisString = iscWindow178sl0.getText().toString();
iscVslText = strThisString;
iscGetTextBox118();
//iscGetTextBox117Done
}


public void iscGetTextBox118()
{
iscWindow178n0 = (EditText)this.findViewById(R.id.iscWindow178n0);
String strThisString = iscWindow178n0.getText().toString();
iscVnText = strThisString;
iscIfThen172();
//iscGetTextBox118Done
}


public void iscOpen_in_Web_Browser120()
{
//iscOpen_in_Web_Browser120Done
}


public void iscAdd123()
{
iscVcount = iscVstart + iscVsl;
iscConvertNumberToText7();
//iscAdd123Done
}


public void iscSubtract124()
{
iscVcount = iscVcount - iscVn1;
//iscSubtract124Done
}


public void iscCombineText125()
{
iscVwrite = iscVwrite + iscVcountText;
//iscCombineText125Done
}


public void iscIfThen126()
{
if (iscVqTest < iscVn)
{
iscCombineText132();
iscPortalDeparture70();
//iscIfThen126True

}
else
{
iscIfThen80();
//iscIfThen126False
}
}


public void iscIfThen127()
{
if (iscVqTest < iscVn)
{
iscCombineText67();
iscPortalDeparture140();
//iscIfThen127True

}
else
{
iscIfThen79();
//iscIfThen127False
}
}


public void iscPortalDestination128()
{
iscSetNumber133();
iscCombineText67();
iscPortalDeparture105();
//iscPortalDestination128Arrived
}


public void iscAdd129()
{
iscVqTest = iscVcount + iscVsl;
//iscAdd129Done
}


public void iscIfThen130()
{
if (iscVwAbout == iscVn1)
{
//iscIfThen130True

}
else
{
iscSetNumber160();
//iscIfThen130False
}
}


public void iscTargetIs131()
{
iscSetNumber165();
iscWindow178();
//iscTargetIs131Android
}


public void iscCombineText132()
{
iscVwrite = iscVwrite + iscVcoma;
//iscCombineText132Done
}


public void iscSetNumber133()
{
iscVqTest = 0;
iscSetNumber134();
//iscSetNumber133Done
}


public void iscSetNumber134()
{
iscVqDifference = 0;
iscSetNumber135();
//iscSetNumber134Done
}


public void iscSetNumber135()
{
iscVcount = iscVstart;
iscConvertNumberToText7();
//iscSetNumber135Done
}


public void iscAdd136()
{
iscVcount = iscVcount + iscVsl;
//iscAdd136Done
}


public void iscAdd137()
{
iscVcount = iscVcount + iscVn1;
//iscAdd137Done
}


public void iscAdd138()
{
iscVn = iscVn + iscVn1;
//iscAdd138Done
}


public void iscPortalDestination139()
{
iscSetNumber133();
iscAdd136();
iscAdd137();
iscAdd138();
iscDoWhile39();
//iscPortalDestination139Arrived
}


public void iscPortalDeparture140()
{
iscPortalDestination141();
//iscPortalDeparture140Done
}


public void iscPortalDestination141()
{
iscAdd136();
iscSubtract124();
iscConvertNumberToText56();
iscCombineText125();
iscPortalDeparture142();
//iscPortalDestination141Arrived
}


public void iscPortalDeparture142()
{
iscPortalDestination143();
//iscPortalDeparture142Done
}


public void iscPortalDestination143()
{
iscAdd129();
iscAdd55();
iscIfThen126();
//iscPortalDestination143Arrived
}


public void iscPortalDestination144()
{
iscSetNumber133();
iscCombineText67();
iscPortalDeparture140();
iscSetText54();
iscCombineText67();
iscAdd129();
iscSubtract51();
iscSubtract52();
iscSubtract124();
iscConvertNumberToText56();
iscCombineText125();
iscSetText49();
//iscPortalDestination144Arrived
}


public void iscConvertTextToNumber145()
{
iscVstart = Integer.parseInt(iscVstartText);
//iscConvertTextToNumber145Done
}


public void iscConvertTextToNumber146()
{
iscVn = Integer.parseInt(iscVnText);
//iscConvertTextToNumber146Done
}


public void iscConvertTextToNumber147()
{
iscVsl = Integer.parseInt(iscVslText);
//iscConvertTextToNumber147Done
}


public void iscGetTextBox148()
{
iscWindow178wImpar0 = (EditText)this.findViewById(R.id.iscWindow178wImpar0);
String strThisString = iscWindow178wImpar0.getText().toString();
iscVwImpar = strThisString;
iscTargetIs175();
//iscGetTextBox148Done
}


public void iscGetTextBox149()
{
iscWindow178wPar0 = (EditText)this.findViewById(R.id.iscWindow178wPar0);
String strThisString = iscWindow178wPar0.getText().toString();
iscVwPar = strThisString;
iscTargetIs176();
//iscGetTextBox149Done
}


public void iscPortalDeparture150()
{
iscPortalDestination6();
//iscPortalDeparture150Done
}


public void iscSetButton152()
{
iscWindow178bStart0 = (Button)this.findViewById(R.id.iscWindow178bStart0);
iscWindow178bStart0.setText(iscVtotalPages);
//iscSetButton152Done
}


public void iscMessageBox153()
{
AlertDialog.Builder alertbox = new AlertDialog.Builder(this);
alertbox.setMessage("The copy button is not available for this platform.");
alertbox.setNeutralButton("Ok", new DialogInterface.OnClickListener() {
public void onClick(DialogInterface arg0, int arg1) {
//iscMessageBox153Closed
}
});
alertbox.show();
}


public void iscMessageBox154()
{
AlertDialog.Builder alertbox = new AlertDialog.Builder(this);
alertbox.setMessage("The copy button is not available for this platform yet. You must copy manually at the moment.");
alertbox.setNeutralButton("Ok", new DialogInterface.OnClickListener() {
public void onClick(DialogInterface arg0, int arg1) {
//iscMessageBox154Closed
}
});
alertbox.show();
}


public void iscTargetIs155()
{
//iscTargetIs155Android
}


public void iscClipboard_Copy157()
{
//iscClipboard_Copy157Done
}


public void iscTargetIs158()
{
iscWindow11();
//iscTargetIs158Android
}


public void iscTargetIs159()
{
iscSubtract19();
iscAdd18();
iscDivide17();
iscIfThen167();
//iscTargetIs159Android
}


public void iscSetNumber160()
{
iscVwAbout = 1;
iscWindow177();
//iscSetNumber160Done
}


public void iscSetCanvasPicture161()
{
iscWindow177icon0.setImageResource(R.drawable.about);
//iscSetCanvasPicture161Done
}


public void iscSetText162()
{
iscVlink = iscVlink_web;
iscTargetIs158();
//iscSetText162Done
}


public void iscSetText163()
{
iscVlink = iscVlink_license;
iscTargetIs158();
//iscSetText163Done
}


public void iscCloseWindow164()
{
//iscCloseWindow164Done
}


public void iscSetNumber165()
{
iscVwAbout = 0;
//iscSetNumber165Done
}


public void iscIfThen167()
{
if (iscVqDifference > iscVcapAndro)
{
//iscIfThen167True

}
else
{
iscIfThen31();
iscSetCanvasPicture8();
//iscIfThen167False
}
}


public void iscIfThen168()
{
if (iscVqDifference > iscVcapApple)
{
//iscIfThen168True

}
else
{
iscIfThen31();
//iscIfThen168False
}
}


public void iscMessageBox171()
{
AlertDialog.Builder alertbox = new AlertDialog.Builder(this);
alertbox.setMessage("Please fill all boxes first.");
alertbox.setNeutralButton("Ok", new DialogInterface.OnClickListener() {
public void onClick(DialogInterface arg0, int arg1) {
//iscMessageBox171Closed
}
});
alertbox.show();
}


public void iscIfThen172()
{
if (iscVstartText == iscVnullText)
{
iscMessageBox171();
//iscIfThen172True

}
else
{
iscIfThen173();
//iscIfThen172False
}
}


public void iscIfThen173()
{
if (iscVnText == iscVnullText)
{
iscMessageBox171();
//iscIfThen173True

}
else
{
iscIfThen174();
//iscIfThen173False
}
}


public void iscIfThen174()
{
if (iscVslText == iscVnullText)
{
iscMessageBox171();
//iscIfThen174True

}
else
{
iscConvertTextToNumber145();
iscConvertTextToNumber146();
iscConvertTextToNumber147();
iscIfThen114();
//iscIfThen174False
}
}


public void iscTargetIs175()
{
iscMessageBox154();
//iscTargetIs175Android
}


public void iscTargetIs176()
{
iscMessageBox154();
//iscTargetIs176Android
}


public void iscWindow178(){
setContentView(R.layout.iscwindow178layout);
iscWindow178n0 = (EditText)this.findViewById(R.id.iscWindow178n0);
iscWindow178n0.setOnKeyListener(new OnKeyListener() {
@Override
public boolean onKey(View v, int keyCode, KeyEvent event) {
//iscWindow178nChanged
return false;
}
});
iscWindow178sl0 = (EditText)this.findViewById(R.id.iscWindow178sl0);
iscWindow178sl0.setOnKeyListener(new OnKeyListener() {
@Override
public boolean onKey(View v, int keyCode, KeyEvent event) {
//iscWindow178slChanged
return false;
}
});
iscWindow178bStart0 = (Button)this.findViewById(R.id.iscWindow178bStart0);
iscWindow178bStart0.setOnClickListener(new OnClickListener() {
@Override
public void onClick(View v) {
iscGetTextBox116();
//iscWindow178bStartClicked
}
});
iscWindow178start0 = (EditText)this.findViewById(R.id.iscWindow178start0);
iscWindow178start0.setOnKeyListener(new OnKeyListener() {
@Override
public boolean onKey(View v, int keyCode, KeyEvent event) {
//iscWindow178startChanged
return false;
}
});
iscWindow178wImpar0 = (EditText)this.findViewById(R.id.iscWindow178wImpar0);
iscWindow178wImpar0.setOnKeyListener(new OnKeyListener() {
@Override
public boolean onKey(View v, int keyCode, KeyEvent event) {
iscSetTextBox78();
//iscWindow178wImparChanged
return false;
}
});
iscWindow178wPar0 = (EditText)this.findViewById(R.id.iscWindow178wPar0);
iscWindow178wPar0.setOnKeyListener(new OnKeyListener() {
@Override
public boolean onKey(View v, int keyCode, KeyEvent event) {
iscSetTextBox102();
//iscWindow178wParChanged
return false;
}
});
iscWindow178CI0 = (ImageView)this.findViewById(R.id.iscWindow178CI0);
iscWindow178CI0.setOnClickListener(new OnClickListener() {
@Override
public void onClick(View v) {
iscGetTextBox148();
//iscWindow178CIClicked
}
});
iscWindow178CP0 = (ImageView)this.findViewById(R.id.iscWindow178CP0);
iscWindow178CP0.setOnClickListener(new OnClickListener() {
@Override
public void onClick(View v) {
iscGetTextBox149();
//iscWindow178CPClicked
}
});
iscWindow178about0 = (Button)this.findViewById(R.id.iscWindow178about0);
iscWindow178about0.setOnClickListener(new OnClickListener() {
@Override
public void onClick(View v) {
iscIfThen130();
//iscWindow178aboutClicked
}
});
iscWindow178paper0 = (Button)this.findViewById(R.id.iscWindow178paper0);
iscWindow178paper0.setOnClickListener(new OnClickListener() {
@Override
public void onClick(View v) {
iscTargetIs50();
//iscWindow178paperClicked
}
});
iscWindow178header0 = (ImageView)this.findViewById(R.id.iscWindow178header0);
iscWindow178header0.setOnClickListener(new OnClickListener() {
@Override
public void onClick(View v) {
//iscWindow178headerClicked
}
});
findViewById(R.id.iscwindow178).setBackgroundColor(Color.argb(255, 0, 0, 0));
iscSetCanvasPicture10();
iscSetCanvasPicture9();
iscSetCanvasPicture8();
//iscWindow178Opened
}

public void iscWindow177(){
setContentView(R.layout.iscwindow177layout);
iscWindow177icon0 = (ImageView)this.findViewById(R.id.iscWindow177icon0);
iscWindow177icon0.setOnClickListener(new OnClickListener() {
@Override
public void onClick(View v) {
//iscWindow177iconClicked
}
});
iscWindow177close0 = (Button)this.findViewById(R.id.iscWindow177close0);
iscWindow177close0.setOnClickListener(new OnClickListener() {
@Override
public void onClick(View v) {
iscTargetIs131();
//iscWindow177closeClicked
}
});
iscWindow177web0 = (Button)this.findViewById(R.id.iscWindow177web0);
iscWindow177web0.setOnClickListener(new OnClickListener() {
@Override
public void onClick(View v) {
iscSetText162();
//iscWindow177webClicked
}
});
iscWindow177license0 = (Button)this.findViewById(R.id.iscWindow177license0);
iscWindow177license0.setOnClickListener(new OnClickListener() {
@Override
public void onClick(View v) {
iscSetText163();
//iscWindow177licenseClicked
}
});
findViewById(R.id.iscwindow177).setBackgroundColor(Color.argb(255, 0, 0, 0));
iscSetCanvasPicture161();
//iscWindow177Opened
}

public void iscWindow11(){
setContentView(R.layout.iscwindow11layout);
iscWindow11return0 = (Button)this.findViewById(R.id.iscWindow11return0);
iscWindow11return0.setOnClickListener(new OnClickListener() {
@Override
public void onClick(View v) {
iscIfThen46();
//iscWindow11returnClicked
}
});
findViewById(R.id.iscwindow11).setBackgroundColor(Color.argb(255, 255, 255, 255));
iscSetWebBrowser47();
//iscWindow11Opened
}

//EndOfFunctions

}
