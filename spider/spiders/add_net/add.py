PK
    j\�F���    _   replacement/modules/uapmdm/META-INF/classes/com/yonyou/impl/mdm07/sharing/MDMService4DI$1.class����   3   -com/yonyou/impl/mdm07/sharing/MDMService4DI$1  !com/google/gson/reflect/TypeToken this$0 -Lcom/yonyou/impl/mdm07/sharing/MDMService4DI; <init> 0(Lcom/yonyou/impl/mdm07/sharing/MDMService4DI;)V Code	    
     ()V LineNumberTable LocalVariableTable this /Lcom/yonyou/impl/mdm07/sharing/MDMService4DI$1; 
SourceFile MDMService4DI.java 	Signature lLcom/google/gson/reflect/TypeToken<Ljava/util/List<Ljava/util/Map<Ljava/lang/String;Ljava/lang/Object;>;>;>; EnclosingMethod  +com/yonyou/impl/mdm07/sharing/MDMService4DI   parseFromJson $(Ljava/lang/String;)Ljava/util/List; InnerClasses                  	   8     
*+� 
*� �       
      �        
                         
        PK
    j\�FT1�D  �D  ]   replacement/modules/uapmdm/META-INF/classes/com/yonyou/impl/mdm07/sharing/MDMService4DI.class����   3~  +com/yonyou/impl/mdm07/sharing/MDMService4DI  java/lang/Object service -Lcom/yonyou/impl/mdm07/sharing/MDMService4DI; sysRegisterServices ELcom/yonyou/itf/mdm0301/building/sysregister/IMDMSysRegisterServices; guiDesignServices ALcom/yonyou/itf/mdm0111/modeling/guidesign/IMDMGuiDesignServices; authorityControlService JLcom/yonyou/itf/mdm0703/sharing/authoritycontrol/IAuthorityControlService; entityModelingServices CLcom/yonyou/itf/mdm0101/modeling/entity/IMDMEntityModelingServices; storeModelService ?Lcom/yonyou/itf/mdm0104/modeling/storemodel/IStoreModelService; storeTableService ?Lcom/yonyou/itf/mdm0102/modeling/storetable/IStoreTableService; mdPersistService ?Lcom/yonyou/itf/mdm0303/building/mdload/IMdOuterPersistService; mdSharingService 0Lcom/yonyou/itf/mdm07/sharing/IMdSharingService; <clinit> ()V Code
     <init>	     LineNumberTable LocalVariableTable
   # Ccom/yonyou/itf/mdm0301/building/sysregister/IMDMSysRegisterServices
 % ' & #uap/lfw/core/locator/ServiceLocator ( ) 
getService %(Ljava/lang/Class;)Ljava/lang/Object;	  +   - ?com/yonyou/itf/mdm0111/modeling/guidesign/IMDMGuiDesignServices	  / 	 
 1 Hcom/yonyou/itf/mdm0703/sharing/authoritycontrol/IAuthorityControlService	  3   5 Acom/yonyou/itf/mdm0101/modeling/entity/IMDMEntityModelingServices	  7   9 =com/yonyou/itf/mdm0104/modeling/storemodel/IStoreModelService	  ;   = =com/yonyou/itf/mdm0102/modeling/storetable/IStoreTableService	  ?   A =com/yonyou/itf/mdm0303/building/mdload/IMdOuterPersistService	  C   E .com/yonyou/itf/mdm07/sharing/IMdSharingService	  G   this getSystemCodeList ()Ljava/lang/String;
  L M  setPortalDataSource " O P Q queryAllSysRegisterVO ()Ljava/util/List;
 S U T ,com/yonyou/impl/mdm07/sharing/VOTransferUtil V W toDIEntityJson $(Ljava/util/List;)Ljava/lang/String; lSysRegisterVO Ljava/util/List; diSystemJson Ljava/lang/String; LocalVariableTypeTable NLjava/util/List<Lcom/yonyou/vo/mdm0301/building/sysregister/MDSysRegisterVO;>; getMDGuiDesignList &(Ljava/lang/String;)Ljava/lang/String; " a b c querySysRegisterVOByCode P(Ljava/lang/String;)Lcom/yonyou/vo/mdm0301/building/sysregister/MDSysRegisterVO;
 e g f :com/yonyou/vo/mdm0301/building/sysregister/MDSysRegisterVO h J getPk_sysregister 0 j k l queryAllAuthorityMDPK #(Ljava/lang/String;)Ljava/util/Set; n java/util/ArrayList
 m  q s r java/util/Set t u size ()I w java/lang/String q y z { toArray (([Ljava/lang/Object;)[Ljava/lang/Object; } [Ljava/lang/String;   com/yonyou/mdm/common/SqlBuilder
 ~  � pk_gd
 ~ � � � append 9(Ljava/lang/String;[Ljava/lang/String;)Ljava/lang/String; , � � � getAggGuiDesignVOByCondition N(Ljava/lang/String;)[Lcom/yonyou/vo/mdm0111/modeling/guidesign/AggGuiDesignVO;
 � � � 7com/yonyou/vo/mdm0111/modeling/guidesign/AggGuiDesignVO � � getParentVO -()Lnc/vo/pub/CircularlyAccessibleValueObject; � 6com/yonyou/vo/mdm0111/modeling/guidesign/MDGuiDesignVO � � � java/util/List � � add (Ljava/lang/Object;)Z
 e � � J getName � "nc/vo/pub/BusinessRuntimeException � java/lang/StringBuilder � 在注册的远程系统[
 � �  � (Ljava/lang/String;)V
 � � � � -(Ljava/lang/String;)Ljava/lang/StringBuilder; � 7]中，找不到有权限的主数据定义列表！！
 � � � J toString
 � �
 S � � W toDIGuiDesignJson outSystemCode sysRegisterVO <Lcom/yonyou/vo/mdm0301/building/sysregister/MDSysRegisterVO; s_pk_guidesigns Ljava/util/Set; lguiDesignVO pk_gds 	condition aggGuiDesignVOs :[Lcom/yonyou/vo/mdm0111/modeling/guidesign/AggGuiDesignVO; aggGuiDesignVO 9Lcom/yonyou/vo/mdm0111/modeling/guidesign/AggGuiDesignVO; guiDesignVO 8Lcom/yonyou/vo/mdm0111/modeling/guidesign/MDGuiDesignVO; 
systemName diGuiDesignJson #Ljava/util/Set<Ljava/lang/String;>; JLjava/util/List<Lcom/yonyou/vo/mdm0111/modeling/guidesign/MDGuiDesignVO;>; StackMapTable � getTableInfoByMDGuiDesignCode , � � � getMDGuiDesignVOByCode L(Ljava/lang/String;)Lcom/yonyou/vo/mdm0111/modeling/guidesign/MDGuiDesignVO;
 � � � J getPk_mdentity 8 � � � queryByEntityPk Q(Ljava/lang/String;)Lcom/yonyou/vo/mdm0104/modeling/storemodel/AggMdStoreModelVO; � -nc/uap/lfw/core/exception/LfwRuntimeException
 � � � uap/lfw/core/ml/LfwResBundle � � getInstance  ()Luap/lfw/core/ml/LfwResBundle; � mdm03 � MdConvertorConfig-000000
 � � � � 
getStrByID 8(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
 v � � � format 9(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;
 � �
 � � � ;com/yonyou/vo/mdm0104/modeling/storemodel/AggMdStoreModelVO � 8com/yonyou/vo/mdm0104/modeling/storemodel/MdStoreModelVO
 � � � J getPk_newtable < � � � queryAggStoreTableByPk Q(Ljava/lang/String;)Lcom/yonyou/vo/mdm0102/modeling/storetable/AggMdStoreTableVO;
 � � � ;com/yonyou/vo/mdm0102/modeling/storetable/AggMdStoreTableVO � 8com/yonyou/vo/mdm0102/modeling/storetable/MdStoreTableVO � MdConvertorConfig-000001
 � � � � getChildrenVO .()[Lnc/vo/pub/CircularlyAccessibleValueObject; � @[Lcom/yonyou/vo/mdm0102/modeling/storetable/MdStoreTableFieldVO;
 �  J getStoretablename
 S toDITableJson :([Lnc/vo/pub/SuperVO;Ljava/lang/String;)Ljava/lang/String; mdmGuiDesignCode voListMapJson aggMdStoreModelVO =Lcom/yonyou/vo/mdm0104/modeling/storemodel/AggMdStoreModelVO; mdStoreModelVO :Lcom/yonyou/vo/mdm0104/modeling/storemodel/MdStoreModelVO; aggStoreTable =Lcom/yonyou/vo/mdm0102/modeling/storetable/AggMdStoreTableVO; 
storeTable :Lcom/yonyou/vo/mdm0102/modeling/storetable/MdStoreTableVO; tableFields postDataFromDI J(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
 S _ gunzip java/util/HashMap
  type java/util/Map  put 8(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;" 
masterData
%'& (com/yonyou/itf/mdm07/sharing/MdmWSLogger() generateLog M(Ljava/lang/String;Ljava/lang/String;Ljava/util/Map;)Ljava/lang/StringBuffer;
%+,- log (Ljava/lang/StringBuffer;)V
 /01 parseFromJson $(Ljava/lang/String;)Ljava/util/List;3 *在MDM中没有对应的主数据定义！
 S567 toDIMessageJson '(ZLjava/lang/String;)Ljava/lang/String;
 �9: J getPk_gd
 <=> setRefMdmCode %(Ljava/lang/String;Ljava/util/List;)V � s �ABC get (I)Ljava/lang/Object; @EFG insert G(Ljava/lang/String;Ljava/lang/String;Ljava/util/Map;)Ljava/lang/String; @IFJ F(Ljava/lang/String;Ljava/lang/String;Ljava/util/List;)Ljava/util/List;
 LMN getIds "(Ljava/util/List;)Ljava/util/List; @PQR 
queryByIds G(Ljava/lang/String;Ljava/lang/String;Ljava/util/List;Z)Ljava/util/List;
 TUV notificateRemoteSystem W(Ljava/lang/String;Lcom/yonyou/itf/mdm07/sharing/MdmDistributeAction;Ljava/util/List;)VX 向MDM系统post数据成功！ compressedStr 
voListJson jsonData params Ljava/util/Map; Ljava/lang/StringBuffer; mdDatas newData 5Ljava/util/Map<Ljava/lang/String;Ljava/lang/Object;>; GLjava/util/List<Ljava/util/Map<Ljava/lang/String;Ljava/lang/Object;>;>;d java/lang/StringBuffer /()Lcom/yonyou/impl/mdm07/sharing/MDMService4DI; 	Signature [(Ljava/lang/String;)Ljava/util/List<Ljava/util/Map<Ljava/lang/String;Ljava/lang/Object;>;>;i com/google/gson/Gson
h l -com/yonyou/impl/mdm07/sharing/MDMService4DI$1
kn o 0(Lcom/yonyou/impl/mdm07/sharing/MDMService4DI;)V
kqrs getType ()Ljava/lang/reflect/Type;
huvw fromJson >(Ljava/lang/String;Ljava/lang/reflect/Type;)Ljava/lang/Object; json gson Lcom/google/gson/Gson;
|~} &nc/uap/portal/util/PortalDsnameFetcher J getPortalDsName
��� *nc/bs/framework/common/InvocationInfoProxy �� .()Lnc/bs/framework/common/InvocationInfoProxy;
��� � setUserDataSource� set portal datasource: 
��� nc/bs/logging/Logger�� info (Ljava/lang/Object;)V ds \(Ljava/lang/String;Ljava/util/List<Ljava/util/Map<Ljava/lang/String;Ljava/lang/Object;>;>;)V
��� .org/apache/commons/collections/CollectionUtils�� isEmpty (Ljava/util/Collection;)Z��� keySet ()Ljava/util/Set; q��� iterator ()Ljava/util/Iterator;��� java/util/Iterator�� next ()Ljava/lang/Object;� $
 v��� indexOf (Ljava/lang/String;)I� body
 v��� 
startsWith (Ljava/lang/String;)Z���� hasNext ()Z ��� \u0024
 v��� split '(Ljava/lang/String;)[Ljava/lang/String;�B� &(Ljava/lang/Object;)Ljava/lang/Object;
��� #org/apache/commons/lang/StringUtils��
c � ,�� � containsKey
 ��� queryMdmcodeByGdCode q(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Lcom/yonyou/itf/mdm07/sharing/MdmRetVO;
��� %com/yonyou/itf/mdm07/sharing/MdmRetVO�� 	isSuccess
��� J getData
c� �� ,(Ljava/lang/String;)Ljava/lang/StringBuffer;
c ���� remove 
systemCode cache map refFieldList subFieldList 	fieldName refField arr gdCode refProp row fieldVal fieldValNew values i I mdmCode mdmRetVO 'Lcom/yonyou/itf/mdm07/sharing/MdmRetVO; subList 5Ljava/util/Map<Ljava/lang/String;Ljava/lang/String;>; $Ljava/util/List<Ljava/lang/String;>;����
� � id
 v�� � equals @��  	queryById H(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Z)Ljava/util/Map; s mdm_code
� � setData
�	
 
setSuccess (Z)V
  � changeToStorageFieldName
 v valueOf &(Ljava/lang/Object;)Ljava/lang/String;  = ' ' @ queryByCondition I(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Z)Ljava/util/List;
�� 
isNotEmpty mdm07  !MdSharingCenterServiceImpl-000004
�"# � 
setMessage% !MdSharingCenterServiceImpl-000000
c' �( ,(Ljava/lang/Object;)Ljava/lang/StringBuffer; "*+ c querySysRegisterVOByPKOrCode	-/. 8com/yonyou/vo/mdm0507/maintaining/mdmlog/MdOperationType01 QUERY :Lcom/yonyou/vo/mdm0507/maintaining/mdmlog/MdOperationType;	354 9com/yonyou/vo/mdm0507/maintaining/mdmlog/MdOperationState67 SUCCESS ;Lcom/yonyou/vo/mdm0507/maintaining/mdmlog/MdOperationState;9 !MdSharingCenterServiceImpl-000005
;=< 4com/yonyou/ctrl/mdm0507/maintaining/mdmlog/MdmLogger,> �(Lcom/yonyou/vo/mdm0507/maintaining/mdmlog/MdOperationType;Lcom/yonyou/vo/mdm0507/maintaining/mdmlog/MdOperationState;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/util/List;)V retVo mdGuiDesignVO md Ljava/lang/Object; storageName extraCondition mdList 
mdmCodeStr systemPk 4IJK getItemsVOByCodeAndParentPK ](Ljava/lang/String;Ljava/lang/String;)Lcom/yonyou/vo/mdm0101/modeling/entity/MDEntityItemsVO;
MON 5com/yonyou/vo/mdm0101/modeling/entity/MDEntityItemsVOP J getPk_mdmentiyitem 8RST queryByEntityItemPk R(Ljava/lang/String;)Lcom/yonyou/vo/mdm0104/modeling/storemodel/MdStoreModelItemVO;
VXW <com/yonyou/vo/mdm0104/modeling/storemodel/MdStoreModelItemVOY J getPk_newtablefield <[\] queryStoreTableFieldByPk S(Ljava/lang/String;)Lcom/yonyou/vo/mdm0102/modeling/storetable/MdStoreTableFieldVO;
_a` =com/yonyou/vo/mdm0102/modeling/storetable/MdStoreTableFieldVOb J getFieldname entityFieldName mdEntityItemsVO 7Lcom/yonyou/vo/mdm0101/modeling/entity/MDEntityItemsVO; storeModelItemVO >Lcom/yonyou/vo/mdm0104/modeling/storemodel/MdStoreModelItemVO; storeTableFieldVO ?Lcom/yonyou/vo/mdm0102/modeling/storetable/MdStoreTableFieldVO; �(Ljava/lang/String;Lcom/yonyou/itf/mdm07/sharing/MdmDistributeAction;Ljava/util/List<Ljava/util/Map<Ljava/lang/String;Ljava/lang/Object;>;>;)Vl null
n �o 0com/yonyou/itf/mdm07/sharing/MdmDistributeAction Dqrs distributeMd e(Ljava/lang/String;Ljava/lang/String;Ljava/util/List;)Lcom/yonyou/itf/mdm07/sharing/OuterSystemRetVO; 
designVoId action 2Lcom/yonyou/itf/mdm07/sharing/MdmDistributeAction; dataList act m(Ljava/util/List<Ljava/util/Map<Ljava/lang/String;Ljava/lang/Object;>;>;)Ljava/util/List<Ljava/lang/String;>; idList 
SourceFile MDMService4DI.java InnerClasses !     	            	 
                                         /      � Y� � �       
    8 
 6               �     e*� !*"� $� "� **,� $� ,� .*0� $� 0� 2*4� $� 4� 6*8� $� 8� :*<� $� <� >*@� $� @� B*D� $� D� F�       * 
   C  9  :  ; ( < 4 = @ > L ? X @ d C         e H     I J     q     *� K*� *� N L+� RM,�           G  H  I  J           H      X Y    Z [  \       X ]   ^ _    �     �*� K*� *+� ` M*� 2,� d� i N� mY� o:-� p � j--� p � v� x � |:� ~Y� ��� �:*� .� � :Y:�6
6	� !	2:� �� �:� � W�		
��ާ ',� �:� �Y� �Y�� �� ��� �� �� ��� �:�       B    O  P  Q  R & S / T C U S V ` W u X  Y � W � ] � ^ � a � b     z    � H      � � [   � � �   � � �  & � � Y  C S � }  S C � [  ` 6 � �  u  � �   
 � �  �  � [  �  � [  \      � � �  & � � �  �   ? � n   v e q � | v �  �  � 	   v e q �  #  � _    s  	   �*� KM*� .+� � N*� :-� ʹ � :� #� �Y� ��۶ �� Y-� �S� � �� �� �:*� >� � � :� �� �:� #� �Y� ���� �� Y-� �S� � �� �� �:� ��M,�       :    g  h  i  j   l % m E o O r _ s i t n u � w � y � {     \ 	   � H      � [   � [   � � �    �	  O V
  _ F  i <  �  �  �    � E v � �� H � � �          �:*� K-�:�Y�:,� W!� W+#�$:�**�.:*� .,� � :		� 2�4:�	�8:
*+�;�? � *� B+
�@ ��D W� *� B+
�H W*� B+
*�K�O :*
�SW�4:�       Z    �  �  �  �  � " � / � : � ? � G � S � X � a � d � k � r � } � � � � � � � � � � �     z    � H      � � [    � [    �Y [   �Z [   �[ [   �\]  : �,^  G �_ Y  S ~ � � 	 k f � [ 
 � ` Y  \       �\a  G �_b  � `b  �   . � d 
  v v v v vc � �  � 3 v 	 �e     $      � �           �        01 f   g    ^     �hY�jM,+�kY*�m�p�t� ��       
    �  �           H      x [   yz   M      `      �{L��+��� �Y�� �+� �� ����           �  �  �  �           H     � [  => f   �   �    �,��� ��Y�N,�@ �:� mY� o:� mY� o:�� �� :� :�� � v:���� � � W���� � � W�� �������� :�	�� � v:���:		2:
	2:	2:,�� :� ��� �:�� � v:��� � ��cY��:Ŷ�:6� m:-2�� � -2�� � v:� 0*+2��:�Ι 
��:-2� W� Ŷ�W��W�����
�ٹ W�� W�� ��0�� ������ ?,�� :� *�� �:�@ �� � �:	*+	�;�� ��ұ       � 0   �  �  �  �  � % � . � K � W � a � l � v � � � � � � � � � � � � � � � � � � � � � � � � � � � � � �) �9 �A �H �V �[ �d �l �w �� � �� ����	�
�	���     �   � H     �� [   �_ Y  ��]  ��]  %�� Y  .�� Y  K +� [  � �� [  � �� } 	 � �� [ 
 � �� [  � �� [  � ��]  � �� [  � ��^  � �� }  u��  d� [ 9 �� � �] � � Y 	 \   R   �_b  ���  ��a  %���  .���  � ��a � �a � �b 	 �  � � 6 	  v � � � �  � ! 	  v � � � v�  �  	  v � � � �  � 2   v � � � v� | v v v �  � $   v � � � v� | v v v� v  � c |� # v� �� � 
�     v � � � v� | v v v �  � 	 	  v � � � �  � 	   v � � �  �  	  v � � � �  &� 	   v � � �   ��    �    �*� K�Y�:�,� W�-� W�� W+��$:��Y��:*� .,� � :�-��� E*� B+�8�� :		� )	� � 	�� :

� v���*,-�:	� �Y	�� �� �� �� �� �:
*� B+�8
� :�� ���cY��:6� >�@ ��� � v:��W�? d� Ŷ�W��? ����ٶ�? � � �� ݶ!� �$� ݶ��&�**� *+�) :� d:�,�2�8� �8� ��:�       � '      % 2 = F R \  p! " �# �$ �& �+ �, �- �. �- �/ �0 �1 �2 �345(612@9J:U;f@C�D�E�F�E�H     �   � H     �� [   �� [   �� [   �� [  �\]  =v,^  Fm?�  Ra@ �  p .A] 	 � �B 
 �C [ 	 � �D [ 
 � �E Y  � sF^  � J��  � [ � ( � � � !G [  \      �\a  p .Aa 	 � �Eb  �   ^ � � 
  v v v vc� �  � � Z   v v v vc� � v v �c  7� 1  �     �     A*� .+� � N*� 6,-� ʹH :*� :�L�Q :*� >�U�Z :�^�          U X [ +^ ;`     H    A H      A� [    Ac [   6@ �   &de  + fg  ; hi  UV f   j    �     ,� 	k� ,�m:*� F+-�p W�          l m n     4     H      t [    uv    w Y   x [  \       wb  �    
C v MN f   y    �     FM+��� >� mY� oM+�� :� !�� �N,-��� � v� � W�� ���,�          q r 	s t 'u :t Dx     *    F H      FE Y   Dz Y  ' A]  \        FEb   Dz�  ' Aa  �   ' �    � � �  � 	   � �   {   |}   
 k      PK
    j\�F��b4V=  V=  \   replacement/modules/uapmdm/META-INF/classes/com/yonyou/impl/mdm07/sharing/MDMService4DI.javapackage com.yonyou.impl.mdm07.sharing;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;

import org.apache.commons.collections.CollectionUtils;
import org.apache.commons.lang.StringUtils;

import nc.bs.framework.common.InvocationInfoProxy;
import nc.bs.logging.Logger;
import nc.uap.lfw.core.exception.LfwRuntimeException;
import nc.uap.portal.util.PortalDsnameFetcher;
import nc.vo.pub.BusinessRuntimeException;
import uap.lfw.core.locator.ServiceLocator;
import uap.lfw.core.ml.LfwResBundle;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import com.yonyou.ctrl.mdm0507.maintaining.mdmlog.MdmLogger;
import com.yonyou.itf.mdm0101.modeling.entity.IMDMEntityModelingServices;
import com.yonyou.itf.mdm0102.modeling.storetable.IStoreTableService;
import com.yonyou.itf.mdm0104.modeling.storemodel.IStoreModelService;
import com.yonyou.itf.mdm0111.modeling.guidesign.IMDMGuiDesignServices;
import com.yonyou.itf.mdm0301.building.sysregister.IMDMSysRegisterServices;
import com.yonyou.itf.mdm0303.building.mdload.IMdOuterPersistService;
import com.yonyou.itf.mdm07.sharing.IMdSharingService;
import com.yonyou.itf.mdm07.sharing.MdmDistributeAction;
import com.yonyou.itf.mdm07.sharing.MdmRetVO;
import com.yonyou.itf.mdm07.sharing.MdmWSLogger;
import com.yonyou.itf.mdm0703.sharing.authoritycontrol.IAuthorityControlService;
import com.yonyou.mdm.common.SqlBuilder;
import com.yonyou.vo.mdm0101.modeling.entity.MDEntityItemsVO;
import com.yonyou.vo.mdm0102.modeling.storetable.AggMdStoreTableVO;
import com.yonyou.vo.mdm0102.modeling.storetable.MdStoreTableFieldVO;
import com.yonyou.vo.mdm0102.modeling.storetable.MdStoreTableVO;
import com.yonyou.vo.mdm0104.modeling.storemodel.AggMdStoreModelVO;
import com.yonyou.vo.mdm0104.modeling.storemodel.MdStoreModelItemVO;
import com.yonyou.vo.mdm0104.modeling.storemodel.MdStoreModelVO;
import com.yonyou.vo.mdm0111.modeling.guidesign.AggGuiDesignVO;
import com.yonyou.vo.mdm0111.modeling.guidesign.MDGuiDesignVO;
import com.yonyou.vo.mdm0301.building.sysregister.MDSysRegisterVO;
import com.yonyou.vo.mdm0507.maintaining.mdmlog.MdOperationState;
import com.yonyou.vo.mdm0507.maintaining.mdmlog.MdOperationType;

/**
 * MDM为DI提供服务的服务类
 * @author wangzhqf
 *
 */

public class MDMService4DI {

	private static final MDMService4DI service = new MDMService4DI();;
	private IMDMSysRegisterServices sysRegisterServices = ServiceLocator.getService(IMDMSysRegisterServices.class);
	private IMDMGuiDesignServices guiDesignServices = ServiceLocator.getService(IMDMGuiDesignServices.class);
	private IAuthorityControlService authorityControlService = ServiceLocator.getService(IAuthorityControlService.class);
	private IMDMEntityModelingServices entityModelingServices = ServiceLocator.getService(IMDMEntityModelingServices.class);
	private IStoreModelService storeModelService = ServiceLocator.getService(IStoreModelService.class);
	private IStoreTableService storeTableService = ServiceLocator.getService(IStoreTableService.class);
	private IMdOuterPersistService mdPersistService = ServiceLocator.getService(IMdOuterPersistService.class);
	private IMdSharingService mdSharingService = ServiceLocator.getService(IMdSharingService.class);
	
	//私有的默认构造器
	private MDMService4DI(){};
	
	public String getSystemCodeList() {
		// 设置portal数据源
				setPortalDataSource();
		List<MDSysRegisterVO> lSysRegisterVO =  (List<MDSysRegisterVO>)sysRegisterServices.queryAllSysRegisterVO();
		String diSystemJson = VOTransferUtil.toDIEntityJson(lSysRegisterVO);
		return diSystemJson;
	}
	
	public String getMDGuiDesignList(String outSystemCode) {
		// 设置portal数据源
				setPortalDataSource();
		MDSysRegisterVO sysRegisterVO = sysRegisterServices.querySysRegisterVOByCode(outSystemCode);
		Set<String> s_pk_guidesigns = authorityControlService.queryAllAuthorityMDPK(sysRegisterVO.getPk_sysregister());
		List<MDGuiDesignVO> lguiDesignVO = new ArrayList<MDGuiDesignVO>();
		if(s_pk_guidesigns.size()>0){
			String[] pk_gds = s_pk_guidesigns.toArray(new String[s_pk_guidesigns.size()]);
			String condition = new SqlBuilder().append(MDGuiDesignVO.PK_GD, pk_gds);
			AggGuiDesignVO[] aggGuiDesignVOs = guiDesignServices.getAggGuiDesignVOByCondition(condition);
			for (AggGuiDesignVO aggGuiDesignVO : aggGuiDesignVOs) {
				MDGuiDesignVO guiDesignVO = (MDGuiDesignVO)aggGuiDesignVO.getParentVO();
				lguiDesignVO.add(guiDesignVO);
			}
		}
		else{
			String systemName = sysRegisterVO.getName();
			throw new BusinessRuntimeException("在注册的远程系统["+systemName+"]中，找不到有权限的主数据定义列表！！");
		}
		
		String diGuiDesignJson = VOTransferUtil.toDIGuiDesignJson(lguiDesignVO);
		return diGuiDesignJson;
	}

	public String getTableInfoByMDGuiDesignCode(String mdmGuiDesignCode) {
		// 设置portal数据源
				setPortalDataSource();
		String voListMapJson = null;
		MDGuiDesignVO guiDesignVO = guiDesignServices.getMDGuiDesignVOByCode(mdmGuiDesignCode);
		AggMdStoreModelVO aggMdStoreModelVO = storeModelService.queryByEntityPk(guiDesignVO.getPk_mdentity());
		// 如果该实体没有对应的存储模型，抛出异常，终止保存操作
		if (aggMdStoreModelVO == null) {
			throw new LfwRuntimeException(String.format(LfwResBundle.getInstance().getStrByID("mdm03", "MdConvertorConfig-000000")/*实体[%s]没有对应的存储模型*/, guiDesignVO.getPk_mdentity()));
		}
		MdStoreModelVO mdStoreModelVO = (MdStoreModelVO) aggMdStoreModelVO.getParentVO();

		// 2.获取表名和列名
		AggMdStoreTableVO aggStoreTable = storeTableService.queryAggStoreTableByPk(mdStoreModelVO.getPk_newtable());
		MdStoreTableVO storeTable = (MdStoreTableVO)aggStoreTable.getParentVO();
		if (storeTable == null) {
			throw new LfwRuntimeException(String.format(LfwResBundle.getInstance().getStrByID("mdm03", "MdConvertorConfig-000001")/*实体[%s]的存储模型关联的存储表定义不存在*/, guiDesignVO.getPk_mdentity()));
		}else{
			MdStoreTableFieldVO[] tableFields = (MdStoreTableFieldVO[])aggStoreTable.getChildrenVO();
			//转化成json串
			voListMapJson = VOTransferUtil.toDITableJson(tableFields, storeTable.getStoretablename());
		}
		return voListMapJson;
	}

	public String postDataFromDI(String outSystemCode, String mdmGuiDesignCode,
			String compressedStr) {
		String voListJson = null;
		//设置portal数据源
		setPortalDataSource();
		
		String jsonData = VOTransferUtil.gunzip(compressedStr);
		//soapui调试用		String jsonData = compressedStr;
		//保存ＷＳ请求数据
		Map<String, Object> params = new HashMap<String, Object>();
		params.put("type", mdmGuiDesignCode);
		params.put("masterData", jsonData);
		StringBuffer log = MdmWSLogger.generateLog(outSystemCode, "postDataFromDI", params);
		MdmWSLogger.log(log);

		//将外部系统的主数据（json）转换成内部需要的格式List<Map<String,Object>>
		List<Map<String, Object>> mdDatas = parseFromJson(jsonData);
		
		//根据界面设计编码查询界面设计PK
		MDGuiDesignVO guiDesignVO = guiDesignServices.getMDGuiDesignVOByCode(mdmGuiDesignCode);
		if(guiDesignVO == null) {
			voListJson = VOTransferUtil.toDIMessageJson(false,"在MDM中没有对应的主数据定义！");
			return voListJson;
		}
		String pk_gd = guiDesignVO.getPk_gd();
		//将从第三方系统来的数据中参数字段的名称设置为主数据编码 
		setRefMdmCode(outSystemCode, mdDatas);
//				Logger.info(mdDatas);
		
		//将转换后的主数据持久化
		if(mdDatas.size() == 1) {	//单条数据不用临时表
			mdPersistService.insert(outSystemCode, pk_gd, mdDatas.get(0));
		} else {
			mdPersistService.insert(outSystemCode, pk_gd , mdDatas);
		}
		
		List<Map<String, Object>> newData = mdPersistService.queryByIds(outSystemCode, pk_gd, getIds(mdDatas), true);
		notificateRemoteSystem(pk_gd, null, newData);
		
		//处理返回值
		voListJson = VOTransferUtil.toDIMessageJson(true,"向MDM系统post数据成功！");
		return voListJson;
	}
	
	public static MDMService4DI getInstance(){
		return service;
	}
	
	/**
	 * 将json格式的主数据转换成List<Map<String, Object>>形式
	 * 
	 * @param json
	 * @return
	 */
	private List<Map<String, Object>> parseFromJson(String json) {
		Gson gson = new Gson();
		return gson.fromJson(json, new TypeToken<List<Map<String, Object>>>(){}.getType());
	}
	
	private void setPortalDataSource() {
		String ds = PortalDsnameFetcher.getPortalDsName();
		InvocationInfoProxy.getInstance().setUserDataSource(ds);
		Logger.info("set portal datasource: " + ds);
	}
	
	/**
	 * 设置第三方系统数据中的参照数据的mdm_code
	 * 
	 * 1、目前第三方系统装载的数据之间的关系是由主数据系统内部根据主数据编码进行维护的，
	 * 后期会将业务数据间关系直接搬到主数据系统内，这里的设置主数据编码就可能不用了 TODO
	 * 
	 * 2、第三方业务数据格式（Excel数据）：
	 * 参照形式：属性:参照实体编码.参照实体中关联字段, 如：type$CompanyType$name
	 * 子表形式：mdm_parentcode:参照实体编码.参照实体中关联字段, 如：mdm_parentcode$Supplier$id
	 * 
	 * @param mdDatas
	 */
	private void setRefMdmCode(String systemCode, List<Map<String, Object>> mdDatas) {
		
		if(CollectionUtils.isEmpty(mdDatas)) {
			return ;
		}
		Map<String, String> cache = new HashMap<String, String>();
		
		//取得参照字段
		Map<String, Object> map = mdDatas.get(0);
		List<String> refFieldList = new ArrayList<String>();
		List<String> subFieldList = new ArrayList<String>();
		for(String fieldName : map.keySet()) {
			if(fieldName.indexOf("$") != -1) {
				refFieldList.add(fieldName);
			}
			if(fieldName.startsWith("body")) {
				subFieldList.add(fieldName);
			}
		}
		if(!CollectionUtils.isEmpty(refFieldList)) {
			for(String refField : refFieldList) {
				String[] arr = refField.split("\\u0024");
				String fieldName = arr[0];
				String gdCode = arr[1];
				String refProp = arr[2];
				for(Map<String, Object> row : mdDatas) {
					String fieldVal = (String) row.get(refField);
					if(StringUtils.isEmpty(fieldVal)) {
						continue;
					}
					//多选参照情况
					StringBuffer fieldValNew = new StringBuffer();
					String[] values = fieldVal.split(",");
					for(int i=0; i<values.length; i++) {
						
						String mdmCode = null;
						if(cache.containsKey(values[i])) {
							mdmCode = cache.get(values[i]);
							
						} else {
							MdmRetVO mdmRetVO = queryMdmcodeByGdCode(systemCode, gdCode, refProp, values[i]);
							if(mdmRetVO.isSuccess()) {
								mdmCode = mdmRetVO.getData();
							}
							cache.put(values[i], mdmCode);						
						}
						
						if(i > 0) {
							fieldValNew.append(",");
						}
						fieldValNew.append(mdmCode);
					}
					row.put(fieldName, fieldValNew.toString());
					row.remove(refField);
				}
			}
		}
		
		//处理子表中的参照数据
		if(!CollectionUtils.isEmpty(subFieldList)) {
			for(Map<String, Object> row : mdDatas) {
				@SuppressWarnings("unchecked")
				List<Map<String, Object>> subList = (List<Map<String, Object>>) row
						.get(subFieldList.get(0));	//目前只支持单子表
				setRefMdmCode(systemCode, subList);
			}
		}
	}
	
public MdmRetVO queryMdmcodeByGdCode(String systemCode, String gdCode, String fieldName, String fieldVal) {
		
		// 设置portal数据源
		setPortalDataSource();
		
		//保存ＷＳ请求数据
		Map<String, Object> params = new HashMap<String, Object>();
		params.put("gdCode", gdCode);
		params.put("fieldName", fieldName);
		params.put("fieldVal", fieldVal);
		StringBuffer log = MdmWSLogger.generateLog(systemCode, "queryMdmcodeByGdCode", params);
		
		MdmRetVO retVo = new MdmRetVO();
		MDGuiDesignVO mdGuiDesignVO = guiDesignServices.getMDGuiDesignVOByCode(gdCode);
		
		if("id".equals(fieldName)) {
			Map<String, Object> md = mdPersistService.queryById(systemCode, mdGuiDesignVO.getPk_gd(), fieldVal, true);
			if(md != null && md.size() > 0) {
				Object mdmCode = md.get("mdm_code");
				retVo.setData((String)mdmCode);
				retVo.setSuccess(true);
			}
			return retVo;
		}
		
		//查询存储表属性名称
		//实体属性名称与存储表名称不一定一致
		String storageName = changeToStorageFieldName(gdCode, fieldName);
		String extraCondition = storageName + " = '" + fieldVal + "'";
		List<Map<String, Object>> mdList = mdPersistService.queryByCondition(systemCode, 
				mdGuiDesignVO.getPk_gd(), extraCondition, false);
		if(CollectionUtils.isNotEmpty(mdList)) {
			retVo.setSuccess(true);
			StringBuffer mdmCodeStr = new StringBuffer();
			for(int i=0; i<mdList.size(); i++) {
				String mdmCode = (String) mdList.get(i).get("mdm_code");
				mdmCodeStr.append(mdmCode);
				if(i != mdList.size() -1) {
					mdmCodeStr.append(",");
				}
			}
			retVo.setData(mdmCodeStr.toString());
			if(mdList.size() > 1) {
				retVo.setMessage(LfwResBundle.getInstance().getStrByID("mdm07", "MdSharingCenterServiceImpl-000004")/*根据名称查询出多条参照数据，请检查参照数据！*/);	//TODO新增一个字段保存message
			}
		}
		
		//记录查询结果
		MdmWSLogger.log(log.append(LfwResBundle.getInstance().getStrByID("mdm07", "MdSharingCenterServiceImpl-000000")/*查询结果：*/).append(retVo));
		
		//将远程系统编码转成系统PK
		MDSysRegisterVO sysRegisterVO = sysRegisterServices.querySysRegisterVOByPKOrCode(systemCode);
		String systemPk = sysRegisterVO.getPk_sysregister();
		MdmLogger.log(MdOperationType.QUERY, MdOperationState.SUCCESS, mdGuiDesignVO.getPk_gd(), systemPk,
				LfwResBundle.getInstance().getStrByID("mdm07", "MdSharingCenterServiceImpl-000005")/*查询主数据编码成功*/, mdList);

		return retVo;
	}

/**
 * 将实体属性名称转换成存储表属性名称
 * 
 * @param gdCode
 * @param entityFieldName
 * @return
 */
private String changeToStorageFieldName(String gdCode, String entityFieldName) {
	
		//根据主数据定义编码取得主实体PK
		MDGuiDesignVO mdGuiDesignVO = guiDesignServices.getMDGuiDesignVOByCode(gdCode);
		
		//根据主实体PK与实体属性名称取得实体属性PK
		MDEntityItemsVO mdEntityItemsVO = entityModelingServices.getItemsVOByCodeAndParentPK(entityFieldName, mdGuiDesignVO.getPk_mdentity());
		
		//根据实体属性PK取得存储表属性PK
		MdStoreModelItemVO storeModelItemVO = storeModelService.queryByEntityItemPk(mdEntityItemsVO.getPk_mdmentiyitem());
		
		//根据存储表属性PK取得存储表属性名称
		MdStoreTableFieldVO storeTableFieldVO = storeTableService.queryStoreTableFieldByPk(storeModelItemVO.getPk_newtablefield());
		
		return storeTableFieldVO.getFieldname();
	}

/**
 * 通知第三方系统数据变化
 * 
 * @param designVoId
 * @param action
 * @param dataList
 */
private void notificateRemoteSystem(String designVoId,
		MdmDistributeAction action, List<Map<String, Object>> dataList) {
	String act = (action == null) ? "null" : action.toString();
	mdSharingService.distributeMd(designVoId, act, dataList);
}

private List<String> getIds(List<Map<String, Object>> mdList) {
	List<String> idList = null;
	if(!CollectionUtils.isEmpty(mdList)) {
		idList = new ArrayList<String>();
		for(Map<String, Object> md : mdList) {
			idList.add((String)md.get("id"));
		}
	}
	return idList;
}
}
PK
    �\�Fz_�   �     installpatch.xml  �       �       <?xml version="1.0" encoding="UTF-8"?>
<installpatch>
<copy><from>/replacement/modules/</from><to>/modules/</to></copy>
</installpatch>
PK
    �\�F            
  readme.txt                  PK
    �\�Ff���      packmetadata.xml              <?xml version="1.0" encoding="UTF-8"?>
<packmetadata>
	<modifiedModules/>
	<department>uap集成应用开发部</department>
	<canAppliedOS>Linux,Windows,AIX,Solaris</canAppliedOS>
	<modifiedJavaClasses>com.yonyou.impl.mdm07.sharing.MDMService4DI,com.yonyou.impl.mdm07.sharing.MDMService4DI$1</modifiedJavaClasses>
	<applyVersion>5.0,5.01,5.011,5.02,5.3,5.5,5.6,5.7,5.75,6.0,6.1,6.3</applyVersion>
	<needRecreatedLoginJar>false</needRecreatedLoginJar>
	<provider>wangzhqf</provider>
	<searchKeys/>
	<needDeploy>false</needDeploy>
	<patchType>Bug Fix Patch</patchType>
	<canAppliedDB>DB2 V9.7,SQL Server 2008 R2,Oracle 10,Oracle 11</canAppliedDB>
	<id>af7f9fae-ef02-43e7-bde1-07d5f9236bda</id>
	<time>2015-06-15 11:38:02</time>
	<dependInfo/>
	<bugs/>
	<patchVersion/>
	<description/>
	<canAppliedMiddleware>Weblogic,Websphere 7.0,Yonyou Middleware V5,Yonyou Middleware V6</canAppliedMiddleware>
	<patchName>找不到design数据源</patchName>
	<patchPriority>High-risk Patch</patchPriority>
</packmetadata>
PK 
    j\�F���    _                 replacement/modules/uapmdm/META-INF/classes/com/yonyou/impl/mdm07/sharing/MDMService4DI$1.classPK 
    j\�FT1�D  �D  ]             �  replacement/modules/uapmdm/META-INF/classes/com/yonyou/impl/mdm07/sharing/MDMService4DI.classPK 
    j\�F��b4V=  V=  \             �H  replacement/modules/uapmdm/META-INF/classes/com/yonyou/impl/mdm07/sharing/MDMService4DI.javaPK 
    �\�Fz_�   �                ]�  installpatch.xmlPK 
    �\�F            
             +�  readme.txtPK 
    �\�Ff���                 g�  packmetadata.xmlPK      V  ��    