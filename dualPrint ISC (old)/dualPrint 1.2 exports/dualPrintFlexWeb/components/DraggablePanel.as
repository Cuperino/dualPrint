package components{
import flash.events.Event;
import flash.events.MouseEvent;
import mx.containers.Panel;
import mx.controls.LinkButton;
public class DraggablePanel extends Panel{
private var _closer:LinkButton=new LinkButton();
[Embed(source="assets/img/close.png")] [Bindable] public var closePng:Class;
public function DraggablePanel(){
super();
_closer.addEventListener(MouseEvent.CLICK, closeMe);
_closer.setStyle('icon', closePng);
_closer.useHandCursor = false;
}
override protected function createChildren():void{
super.createChildren();
super.titleBar.addEventListener(MouseEvent.MOUSE_DOWN,handleDown);
super.titleBar.addEventListener(MouseEvent.MOUSE_UP,handleUp);
super.titleBar.addChild(_closer);
}
override protected function updateDisplayList(unscaledWidth:Number, unscaledHeight:Number):void{
super.updateDisplayList(unscaledWidth,unscaledHeight);
_closer.width = 16;
_closer.height = 16;
_closer.x = super.titleBar.width - _closer.width - 8;
_closer.y = 8;
}
private function handleDown(e:Event):void{
this.startDrag();
}
private function handleUp(e:Event):void{
this.stopDrag();
}
private function closeMe(e:MouseEvent):void{
this.visible = false;
}
}
}
