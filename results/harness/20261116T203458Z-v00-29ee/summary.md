# Harness run 20261116T203458Z-v00-29ee

- Task: refresh
- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: 082095c0494b089e8303c0f6733826318c965814
- Notebook run: 44a338bf-58fc-42ca-acb4-1981ae5f2a49
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request e87de7e6-eba8-433a-90ec-44c295266aab, 2026-11-16T20:37:16.84Z to 2026-11-16T20:38:09.73Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v00-baseline on Pro data-1m-v1.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-16T20:37:01Z run 20261116T203458Z-v00-29ee: variant=v00-baseline data_tag=data-1m-v1 targets=['Pro'] expected_commit=082095c0494b089e8303c0f6733826318c965814
2026-11-16T20:37:04Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-16T20:37:05Z Pro: v00-baseline is d617fd07-8a52-4fda-ab69-2b58d0426997, DataTag reads back data-1m-v1
2026-11-16T20:37:16Z Pro: model size in memory before the refresh: None MB
2026-11-16T20:37:16Z Pro: standard refresh started
2026-11-16T20:38:17Z Pro: refresh refreshed (Completed) 
2026-11-16T20:38:20Z Pro: model size query failed: An error occurred when running AdomdCommand. AdomdCommandActivityId: '6a017f0d-1cde-4432-bcca-096ace66f56b'

Caused by AdomdErrorResponseException:
The '<euii><user></euii>' user does not have permission to call the Discover method.

Technical Details:
RootActivityId: 38eba74f-b593-4e74-9fce-97a9d3df0a6c
Date (UTC): 11/16/2026 8:38:20 PM
   at Microsoft.AnalysisServices.AdomdClient.XmlaClient.CheckForSoapFault(XmlReader reader, XmlaResult xmlaResult, Boolean throwIfError)
   at Microsoft.AnalysisServices.AdomdClient.XmlaClient.CheckForError(XmlReader reader, XmlaResult xmlaResult, Boolean throwIfError)
   at Microsoft.AnalysisServices.AdomdClient.XmlaClient.SendMessage(Boolean endReceivalIfException, Boolean readSession, Boolean readNamespaceCompatibility)
   at Microsoft.AnalysisServices.AdomdClient.XmlaClient.ExecuteStatement(String statement, IDictionary connectionProperties, IDictionary commandProperties, IDataParameterCollection parameters, Boolean isMdx)
   at Microsoft.AnalysisServices.AdomdClient.AdomdConnection.XmlaClientProvider.Microsoft.AnalysisServices.AdomdClient.IExecuteProvider.ExecuteTabular(CommandBehavior behavior, ICommandContentProvider contentProvider, AdomdPropertyCollection commandProperties, IDataParameterCollection parameters)
   at Microsoft.AnalysisServices.AdomdClient.AdomdCommand.ExecuteReader(CommandBehavior behavior)
   at Microsoft.AnalysisServices.AdomdClient.AdomdCommand.ExecuteReader()
   at Microsoft.Fabric.SemanticLink.DAXToParquetWriter.Write(String dax, String fileName, Int32 batchSize, AdomdConnection adomdConnection, Int32 verbose, Nullable`1 maxNumRows, Nullable`1 activityId)
   at System.RuntimeMethodHandle.InvokeMethod(Object target, Void** arguments, Signature sig, Boolean isConstructor)
   at System.Reflection.MethodBaseInvoker.InvokeWithManyArgs(Object obj, BindingFlags invokeAttr, Binder binder, Object[] parameters, CultureInfo culture)

2026-11-16T20:38:20Z Pro: model size in memory right after the refresh: None MB
```
